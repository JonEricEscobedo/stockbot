import requests

def fetch_api_data(ticker):
    quote_url = 'https://api.iextrading.com/1.0/stock/{STOCK}/batch?types=quote,chart&range=1y'.format(STOCK=ticker)
    logo_url = 'https://api.iextrading.com/1.0/stock/{STOCK}/logo'.format(STOCK=ticker)

    raw_response = requests.get(quote_url).json()
    logo = requests.get(logo_url).json()

    return {
        'raw_response': raw_response,
        'raw_quote': raw_response['quote'],
        'raw_chart': raw_response['chart'],
        'logo': logo
    }
