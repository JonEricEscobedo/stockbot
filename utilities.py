import datetime

def calculate_date(quote_date, chart_date):
    quote_date_human_readable = str(datetime.datetime.fromtimestamp(quote_date / 1000).strftime('%Y-%m-%d'))

    ###
    ### TODO: Double check this! Might be creating false positives when the market closes for the day.
    ###

    if (quote_date_human_readable == chart_date):
        return True
    else:
        return False

def determine_verbal_analysis(lower, upper, actual):
    if (lower > actual):
        return 'of going up'
    elif (upper < actual):
        return 'of going down'
    else:
        return 'no major change'
