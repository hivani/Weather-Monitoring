import matplotlib.pyplot as plt

def plot_summary(summary):
    cities = summary.index
    avg_temp = summary[('temperature', 'mean')]
    
    plt.figure(figsize=(10, 5))
    plt.bar(cities, avg_temp, color='blue')
    plt.xlabel('City')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Daily Average Temperatures by City')
    plt.show()

if __name__ == "__main__":
    from weather_aggregator import aggregate_daily_weather
    from weather_api import fetch_weather_for_cities
    data = fetch_weather_for_cities()
    summary = aggregate_daily_weather(data)
    plot_summary(summary)