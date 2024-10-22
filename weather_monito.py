import time
from weather_api import fetch_weather, process_weather_data, CITIES

FETCH_INTERVAL = 300  # 5 minutes in seconds

def fetch_weather_for_cities():
    weather_data = []
    for city in CITIES:
        try:
            data = fetch_weather(city)
            processed_data = process_weather_data(data)
            weather_data.append(processed_data)
        except Exception as e:
            print(f"Error fetching data for {city}: {e}")
    return weather_data

def continuous_fetch():
    while True:
        try:
            weather_data = fetch_weather_for_cities()
            print(weather_data)  # Or process the data further here
            time.sleep(FETCH_INTERVAL)
        except Exception as e:
            print(f"Error in continuous fetch loop: {e}")
            break  # Optional: break if you want to exit on error

if __name__ == "__main__":
    continuous_fetch()
