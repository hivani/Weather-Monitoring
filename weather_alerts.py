ALERT_TEMP_THRESHOLD = 35  # Example threshold for temperature in Celsius

def check_alerts(weather_data):
    for entry in weather_data:
        if entry['temperature'] > ALERT_TEMP_THRESHOLD:
            print(f"Alert! Temperature in {entry['city']} exceeds {ALERT_TEMP_THRESHOLD}°C")
            # You can add an email alert system here if needed

if __name__ == "__main__":
    from weather_api import fetch_weather_for_cities
    data = fetch_weather_for_cities()
    check_alerts(data)