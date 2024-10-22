from weather_api import fetch_weather, process_weather_data

city_weather = fetch_weather("london")
processed_data = process_weather_data(city_weather)
print(processed_data)
