from flask import Flask, app, jsonify, request
import requests

from weather_aggregator import aggregate_daily_weather
from weather_api import API_KEY, process_weather_data
from weather_monito import fetch_weather_for_cities

@app.route('/api/weather-summary', methods=['GET'])
def weather_summary():
    city = request.args.get('city')
    if city:
        # Fetch and summarize weather data for the specific city
        data = fetch_weather(city)  # Create a new function to fetch weather for a single city
        summary = aggregate_daily_weather([data])  # Wrap in a list for aggregation

        # Convert summary DataFrame to a JSON-friendly format
        result = summary.reset_index().to_dict(orient='records')
        return jsonify(result)
    else:
        # Return summary for all cities if no city parameter is provided
        all_data = fetch_weather_for_cities()
        summary = aggregate_daily_weather(all_data)
        result = summary.reset_index().to_dict(orient='records')
        return jsonify(result)

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return process_weather_data(response.json())
