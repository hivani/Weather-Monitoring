import pandas as pd

daily_data = {
    "city": [],
    "temperature": [],
    "feels_like": [],
    "weather_condition": [],
    "timestamp": []
}

def aggregate_daily_weather(weather_data):
    global daily_data
    
    for entry in weather_data:
        daily_data['city'].append(entry['city'])
        daily_data['temperature'].append(entry['temperature'])
        daily_data['feels_like'].append(entry['feels_like'])
        daily_data['weather_condition'].append(entry['weather_condition'])
        daily_data['timestamp'].append(pd.to_datetime(entry['timestamp'], unit='s').date())

    df = pd.DataFrame(daily_data)

    summary = df.groupby('city').agg({
        'temperature': ['mean', 'max', 'min'],
        'weather_condition': lambda x: x.mode()[0]  # Dominant weather condition (mode)
    })

    return summary
if __name__ == "__main__":
    from weather_api import fetch_weather_for_cities
    data = fetch_weather_for_cities()
    summary = aggregate_daily_weather(data)
    print(summary)