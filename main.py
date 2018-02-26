import logging
import jinja2
import os
import urllib2
import requests
import requests_toolbelt.adapters.appengine
# tutorial
from random import *
# /tutorial

from flask import Flask, render_template, jsonify
from flask_cors import CORS

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

app = Flask(__name__)
cors = CORS(app, resources={r'/api/*': {'origins': '*'}})
app.jinja_loader = jinja2.FileSystemLoader('app/dist')

# API Route `/api/data/stock` - Fetches stock quote and logo
@app.route('/api/data/stock')
def fetch_quote():
    raw_stock_quote_response = requests.get('https://api.iextrading.com/1.0/stock/nvda/batch?types=quote').json()
    raw_stock_logo_response = requests.get('https://api.iextrading.com/1.0/stock/nvda/logo').json()
    stock_quote_high = raw_stock_quote_response['quote']['high']
    stock_quote_low = raw_stock_quote_response['quote']['low']
    stock_quote_avg = str(round((stock_quote_high + stock_quote_low) / 2, 2))

    response = {
        'stock': {
            'logo': raw_stock_logo_response['url'],
            'ticker': raw_stock_quote_response['quote']['symbol'],
            'company': raw_stock_quote_response['quote']['companyName'],
            'quote': stock_quote_avg
        }
    }

    return jsonify(response)

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
