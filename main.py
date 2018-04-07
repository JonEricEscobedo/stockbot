import logging
import jinja2
import os
import urllib2
import requests
import requests_toolbelt.adapters.appengine
import datetime

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

app = Flask(__name__)
cors = CORS(app, resources={r'/api/*': {'origins': '*'}})
app.jinja_loader = jinja2.FileSystemLoader('app/dist')

# Prediction algorithms
def predict_stock_algorithm_1(p, p_1):
    # Step 1
    # delta = (p - p-1) / (t - t-1) where (t-t-1) will equal 1
    delta = (p - p_1) / 1

    # Step 2
    # p+1 = ((delta )(t+1-t)) + p
    p_predict = ((delta)*1) + p
    return p_predict

# Utility functions
def calculate_average(high, low):
    return round(((high + low) / 2), 2)

def calculate_date(quote_date, chart_date):
    quote_date_human_readable = str(datetime.datetime.fromtimestamp(quote_date / 1000).strftime('%Y-%m-%d'))
    if (quote_date_human_readable == chart_date):
        return True
    else:
        return False

def calculate_error(today, yesterday):
    today_avg = calculate_average(today['high'], today['low'])
    yesterday_avg = calculate_average(yesterday['high'], yesterday['low'])

    # error = predicted value - actual value
    return round((predict_stock_algorithm_1(today_avg, yesterday_avg) - today_avg), 2)

def fetch_quote_extended(symbol):
    ticker = symbol
    quote_url = 'https://api.iextrading.com/1.0/stock/{STOCK}/batch?types=chart&range=6m'.format(STOCK=ticker)

    raw_quote_response = requests.get(quote_url).json()
    chart_quotes = raw_quote_response['chart']
    chart_length = len(chart_quotes) - 1

    error_data_points = []

    for i in range(chart_length, chart_length - 100, -1):
        error_data_points.append(calculate_error(chart_quotes[i], chart_quotes[i - 1])) # TODO: What about the current daily quote??? Charts doesn't get updated until the end...

    return error_data_points

# API Route `/api/data/stock` - Fetches stock quote and logo
@app.route('/api/data/stock')
def fetch_quote():
    # Get ticker symbol from FE
    ticker = request.args.get('ticker')
    quote_url = 'https://api.iextrading.com/1.0/stock/{STOCK}/batch?types=quote,chart&range=6m'.format(STOCK=ticker)
    logo_url = 'https://api.iextrading.com/1.0/stock/{STOCK}/logo'.format(STOCK=ticker)

    # Fetch stock quote
    raw_quote_response = requests.get(quote_url).json()
    raw_logo_response = requests.get(logo_url).json()

    # Calculate today's stock quote average
    quote_high = raw_quote_response['quote']['high']
    quote_low = raw_quote_response['quote']['low']
    quote_avg = str(calculate_average(quote_high, quote_low))

    # Is it a weekend and the markets are closed?
    is_weekend = calculate_date(raw_quote_response['quote']['closeTime'], raw_quote_response['chart'][-1]['date'])
    print('Market Closed? (Weekend detected?)', is_weekend)

    # Calculate yesterday's stock quote average
    if (is_weekend):
        quote_yesterday_high = (raw_quote_response['chart'])[-2]['high']
        quote_yesterday_low = (raw_quote_response['chart'])[-2]['low']
    else:
        quote_yesterday_high = (raw_quote_response['chart'])[-1]['high']
        quote_yesterday_low = (raw_quote_response['chart'])[-1]['low']

    quote_yesterday_avg = str(calculate_average(quote_yesterday_high, quote_yesterday_low))

    # Prediction algorithm #1
    quote_prediction = str(predict_stock_algorithm_1(float(quote_avg), float(quote_yesterday_avg)))

    # Calculate error for 100 data points
    error_data_points = fetch_quote_extended(ticker)

    response = {
        'stock': {
            'logo': raw_logo_response['url'],
            'ticker': raw_quote_response['quote']['symbol'],
            'company': raw_quote_response['quote']['companyName'],
            'quote': quote_avg,
            'date': raw_quote_response['quote']['latestTime']
        },
        'prediction': {
            'tomorrow_avg': quote_prediction
        }
    }

    return jsonify(response)

# API Route `/api/data/scientist` - Returns raw TSLA stock response for the data scientist
@app.route('/api/data/scientist')
def fetch_quote_scientist():
    custom_quote_url = 'https://api.iextrading.com/1.0/stock/tsla/batch?types=quote,chart&range=1m'
    raw_quote_response = requests.get(custom_quote_url).json()

    return jsonify(raw_quote_response)

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
