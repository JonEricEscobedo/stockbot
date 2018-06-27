import logging
import jinja2
import os
import urllib2
import requests
import requests_toolbelt.adapters.appengine
import numpy as np

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

from algorithms import prediction_algorithm_1, prediction_algorithm_2, prediction_algorithm_3
from fetch import fetch_api_data
from statistics import calculate_average
from utilities import calculate_date, determine_verbal_analysis

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

app = Flask(__name__)
cors = CORS(app, resources={r'/api/*': {'origins': '*'}})
app.jinja_loader = jinja2.FileSystemLoader('app/dist')

# Statistics functions
def get_lower_and_upper_limit(error_series):
    dZ = 1.96

    #Calculate Mean
    mean = np.mean(error_series)

    #Calculate Stvd
    std_dev = np.std(error_series, ddof=1)

    #Calculate Upper Limit
    upper_limit = mean + (std_dev * dZ)

    #Calculate Lower Limit
    lower_limit = mean - (std_dev * dZ)

    #Return u,l
    return (lower_limit, upper_limit)

success_vote = 0.0
failure_vote = 0.0
def algo_success(lower_limit, upper_limit, error_t):
    global success_vote
    global failure_vote
    #see if error t is within upper limit and lower limit
    if error_t >= lower_limit and error_t <= upper_limit:
        #increment success vote
        success_vote = success_vote + 1.0
    else:
        #increment failure vote
        failure_vote = failure_vote + 1.0
    #prob of success vote (success/ (Success+failure))
    total = success_vote + failure_vote

    probability = float(success_vote) / float(total)

    return (probability)

def calculate_error(today, yesterday):
    today_avg = calculate_average(today)
    yesterday_avg = calculate_average(yesterday)

    # error = predicted value - actual value
    return round((prediction_algorithm_1(today_avg, yesterday_avg) - today_avg), 2)

def fetch_error_points(chart_data):
    chart_length = len(chart_data) - 1

    error_points = []

    for i in range(chart_length - 1, chart_length - 200, -1):
        # error_points.append(calculate_error(chart_data[i], chart_data[i - 1]))
        error_points.insert(0, calculate_error(chart_data[i], chart_data[i - 1]))

    return error_points

def fetch_and_average_prices(chart_data, today_avg):
    arr_len = len(chart_data) - 1
    results = []
    for i in range(arr_len - 1, arr_len - 200, - 1):
        results.insert(0, calculate_average(chart_data[i]))

    results.append(today_avg)
    return results;

def predict_prices(predictive_algorithm, actual_averages):
    arr_len = len(actual_averages)
    results = []
    for p in range(1, arr_len):
        results.append(predictive_algorithm(actual_averages[p], actual_averages[p - 1]))

    results.insert(0, None)
    results.insert(0, None)
    return results;

def fetch_error_points_extended(predicted, actual):
    arr_len = len(actual)
    results = []
    for i in range(arr_len):
        if predicted[i] != None:
            results.append(round(predicted[i] - actual[i], 2))

    return results;

def get_prediction(prediction_algorithm, params, isAdvancedAlgo = False):
    # calculate prediction
    if (isAdvancedAlgo):
        predicted_price = prediction_algorithm(params['predicted_values'], params['actual_values'], params['error_p_a'])
    else:
        predicted_price = prediction_algorithm(params['today_avg'], params['yesterday_avg'])

    # calculate error
    error_series = fetch_error_points(params['raw_chart_response'])

    # calculate l and u limits
    error_series.append(round((predicted_price - params['today_avg']), 2)) # Append the array w/ the latest daily values
    lower_and_upper_limits = get_lower_and_upper_limit(error_series[100:200])

    lower_range = predicted_price - abs(lower_and_upper_limits[0])
    upper_range = predicted_price + lower_and_upper_limits[1]

    # calculate probability
    for i in range(len(error_series) - 1, len(error_series) - 101, -1):
        lu = get_lower_and_upper_limit(error_series[i-100:i])
        probability = algo_success(lu[0], lu[1], error_series[i])
        verbal_analysis = determine_verbal_analysis(lower_range, upper_range, params['today_avg'])

    return {
        'predicted_price': predicted_price,
        'lower_and_upper_limits': lower_and_upper_limits,
        'lower_range': lower_range,
        'upper_range': upper_range,
        'probability': probability,
        'verbal_analysis': verbal_analysis
    }

# API Route `/api/data/stock` - Fetches stock quote and logo
@app.route('/api/data/stock')
def fetch_quote():
    # Get ticker symbol from FE
    ticker = request.args.get('ticker')
    data = fetch_api_data(ticker)

    # Calculate today's stock quote average
    today_avg = calculate_average(data['raw_quote'])

    # Is it a weekend and the markets are closed?
    is_weekend = calculate_date(data['raw_quote']['closeTime'], data['raw_chart'][-1]['date'])
    # print('Market Closed? (Weekend detected?)', is_weekend)

    # Calculate yesterday's stock quote average
    if (is_weekend):
        yesterday_avg = calculate_average(data['raw_chart'][-2])
    else:
        yesterday_avg = calculate_average(data['raw_chart'][-1])

    standard_params = {
        'today_avg': today_avg,
        'yesterday_avg': yesterday_avg,
        'raw_chart_response': data['raw_chart']
    }

    actual_averages = fetch_and_average_prices(data['raw_chart'], today_avg);
    predicted_averages = predict_prices(prediction_algorithm_1, actual_averages)
    error_p_a = fetch_error_points_extended(predicted_averages, actual_averages)

    custom_params = {
        'predicted_values': predicted_averages[101:],
        'actual_values': actual_averages[101:],
        'error_p_a': error_p_a[0:99],
        'today_avg': today_avg,
        'yesterday_avg': yesterday_avg,
        'raw_chart_response': data['raw_chart']
    }

    # Prediction algorithm #1
    prediction_1 = get_prediction(prediction_algorithm_1, standard_params)

    # Prediction algorithm #2
    prediction_2 = get_prediction(prediction_algorithm_2, standard_params)

    # Prediction algorithm #3
    prediction_3 = get_prediction(prediction_algorithm_3, custom_params, True)

    response = {
        'stock': {
            'logo': data['logo']['url'],
            'ticker': data['raw_quote']['symbol'],
            'company': data['raw_quote']['companyName'],
            'quote': str(today_avg),
            'date': data['raw_quote']['latestTime']
        },
        'predictions': {
            'prediction1': {
                'tomorrow_avg': str(prediction_1['predicted_price']),
                'limits': prediction_1['lower_and_upper_limits'],
                'lower_range': round(prediction_1['lower_range'], 2),
                'upper_range': round(prediction_1['upper_range'], 2),
                'probability': round(prediction_1['probability'] * 100, 0),
                'verbal_analysis': prediction_1['verbal_analysis']
            },
            'prediction2': {
                'tomorrow_avg': str(prediction_2['predicted_price']),
                'limits': prediction_2['lower_and_upper_limits'],
                'lower_range': round(prediction_2['lower_range'], 2),
                'upper_range': round(prediction_2['upper_range'], 2),
                'probability': round(prediction_2['probability'] * 100, 0),
                'verbal_analysis': prediction_2['verbal_analysis']
            },
            'prediction3': {
                'tomorrow_avg': str(prediction_3['predicted_price']),
                'limits': prediction_3['lower_and_upper_limits'],
                'lower_range': round(prediction_3['lower_range'], 2),
                'upper_range': round(prediction_3['upper_range'], 2),
                'probability': round(prediction_3['probability'] * 100, 0),
                'verbal_analysis': prediction_3['verbal_analysis']
            }
        }
    }

    return jsonify(response)

# API Route `/api/data/scientist` - Returns raw TSLA stock response for the data scientist
@app.route('/api/data/scientist')
def fetch_quote_scientist():
    custom_quote_url = 'https://api.iextrading.com/1.0/stock/tsla/batch?types=quote,chart&range=1m'
    raw_response = requests.get(custom_quote_url).json()

    return jsonify(raw_response)

# Serves up Vue frontend on application load
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def vue_client(path):
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        return render_template('index.html')
    else:
        url = 'http://localhost:3000/{0}'.format(path)
        return urllib2.urlopen(url).read()

# Error handling
@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
