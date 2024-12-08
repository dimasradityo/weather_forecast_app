import requests

API_KEY = '34ba92ce17c552cd0106fbd94a646f58'

def get_weather_data (place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == '__main__':
    print(get_weather_data('jakartax', 3))