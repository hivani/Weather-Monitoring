import sqlite3

def store_summary(summary):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather_summary (
            city TEXT,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
    ''')

    for city, data in summary.iterrows():
        avg_temp = data[('temperature', 'mean')]
        max_temp = data[('temperature', 'max')]
        min_temp = data[('temperature', 'min')]
        dominant_condition = data[('weather_condition', '<lambda>')]

        c.execute('''
            INSERT INTO weather_summary (city, avg_temp, max_temp, min_temp, dominant_condition)
            VALUES (?, ?, ?, ?, ?)
        ''', (city, avg_temp, max_temp, min_temp, dominant_condition))

    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    from weather_aggregator import aggregate_daily_weather
    from weather_api import fetch_weather_for_cities
    data = fetch_weather_for_cities()
    summary = aggregate_daily_weather(data)
    store_summary(summary)