import datetime
import json
import os
import numpy as np
import requests
import matplotlib.pyplot as plt

username = "leave_me_here"
start_date = "2021-03-23"
custom_dpi = 300

def date_to_js_timestamp(date_str):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    return (date - datetime.date(1970, 1, 1)).total_seconds()

def js_timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

def generate_data(username, start_date_input):
    today = datetime.datetime.today()
    tomorrow = today + datetime.timedelta(days=1)
    tomorrow_date = tomorrow.strftime("%Y-%m-%d")

    end_date = int(date_to_js_timestamp(tomorrow_date))
    start_date = int(date_to_js_timestamp(start_date_input))
    print("start date:", js_timestamp_to_date(start_date))

    base_url = "https://data.typeracer.com/games?playerId=tr:" + username + "&universe=play&startDate="

    data = []
    while True:
        print("trying to fetch 1000 race events backwards from", js_timestamp_to_date(end_date), "...")
        url = base_url + str(start_date) + "&endDate=" + str(end_date)
        response = requests.get(url)
        if response.status_code == 200:
            curr_data = response.json()
            data.extend(curr_data)
            if curr_data[-1]["gn"] == 1:
                print("completed successfully")
                break
            end_date = int(curr_data[-1]["t"])
        else:
            break
    if not os.path.exists('exports'):
        os.makedirs('exports')
    with open('./exports/data.json', 'w') as file:
        json.dump(data, file, indent=4)
    return data

def main():
    ## function calling with user_name and start_date for results
    data = generate_data(username, start_date)

    print("total no of races:", len(data))

    data = data[::-1]

    # Plot the data

    x = np.array([d['gn'] for d in data])
    y = np.array([d['wpm'] for d in data])

    # Calculate the average window size
    if len(x) > 10000:
        average_window = len(x) // 200 + 1
    elif 5000 < len(x) <= 10000:
        average_window = len(x) // 100 + 1
    elif 1000 < len(x) < 5000:
        average_window = len(x) // 80 + 1
    elif 100 < len(x) < 1000:
        average_window = len(x) // 50 + 1
    elif len(x) < 100:
        average_window = len(x) // 10 + 1

    # print(average_window)

    # Calculate the number of averages
    num_averages = len(x) // average_window

    # Truncate the arrays to ensure they are divisible by 10
    x_truncated = x[:num_averages*average_window]
    y_truncated = y[:num_averages*average_window]

    # Reshape the arrays to average every 10 values
    x_averages = x_truncated.reshape(num_averages, average_window).mean(axis=1)
    y_averages = y_truncated.reshape(num_averages, average_window).mean(axis=1)

    if len(x_truncated) < len(x):
        x_remaining = x[num_averages*average_window:]
        y_remaining = y[num_averages*average_window:]

        x_averages = np.append(x_averages, x_remaining.mean())
        y_averages = np.append(y_averages, y_remaining.mean())
    
    plt.figure(figsize=(4, 2), dpi=custom_dpi)
    
    plt.plot(x_averages, y_averages)
    plt.xlabel("race number")
    plt.ylabel("wpm")
    # plt.title("Typeracer WPM over time")
    
    if not os.path.exists('exports'):
        os.makedirs('exports')

    plt.savefig('./exports/light_graph.png', dpi=custom_dpi, bbox_inches='tight')

    plt.clf()
    plt.style.use('dark_background')
    plt.plot(x_averages, y_averages)
    plt.xlabel("race number")
    plt.ylabel("wpm")
    # plt.title("Typeracer WPM over time")

    plt.savefig('./exports/dark_graph.png', dpi=custom_dpi, bbox_inches='tight')
    return

if __name__ == "__main__":
    main()
