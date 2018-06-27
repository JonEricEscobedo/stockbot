import numpy as np

def prediction_algorithm_1(today_avg, yesterday_avg):
    # Step 1
    # delta = (p - p-1) / (t - t-1) where (t-t-1) will equal 1
    delta = (today_avg - yesterday_avg) / 1

    # Step 2
    # p+1 = ((delta )(t+1-t)) + p
    p_predict = (delta * 1) + today_avg
    return p_predict

def prediction_algorithm_2(today_avg, yesterday_avg):
    #step 1
    #n, where n = sample size for the time period, we are looking at
    n = 2.0
    #step 2
    #calculate k, where k = 2/(N+1)
    k = 2.0 / (n + 1.0)

    #step 3
    #EMA = (current close price x K)+(ema yesterdayx(1-k))
    ema = (today_avg * k) + (yesterday_avg * (1 - k))
    return ema

def prediction_algorithm_3(predicted_values, actual_values, error_p_a):
    mean_error_array = [0]
    new_predicted_price_array = []

    # calc mean error of first one hundred error values
    for i in range(0, 99):
        # Calculate new predicted price using i-1 mean error point
        new_predicted_value = predicted_values[0 + i] - mean_error_array[0 + i]
        new_predicted_price_array.append(new_predicted_value)

        # Calculate new P - A
        new_error = new_predicted_value - actual_values[0 + i]
        error_p_a.append(new_error)

        # Get mean average of 100 error points
        current_mean_error = np.average(error_p_a[0 + i : 100 + i]);

        # Repeat
        mean_error_array.append(current_mean_error)

    predicted_price = prediction_algorithm_1(actual_values[98], actual_values[97]) - mean_error_array[-1]
    return predicted_price
