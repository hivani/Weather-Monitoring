import requests

API_KEY = "4695e7f0e85fb5cfa1f2d598aa6bb8c9"  # Replace with your OpenWeatherMap API Key
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

def process_weather_data(data):
    city = data['name']
    temp = kelvin_to_celsius(data['main']['temp'])
    feels_like = kelvin_to_celsius(data['main']['feels_like'])
    weather_condition = data['weather'][0]['main']
    timestamp = data['dt']  # Unix timestamp
    return {
        "city": city,
        "temperature": temp,
        "feels_like": feels_like,
        "weather_condition": weather_condition,
        "timestamp": timestamp
    }
def fetch_weather_for_cities():
    weather_data = []
    for city in CITIES:
        data = fetch_weather(city)
        weather_data.append(process_weather_data(data))
    return weather_data

if __name__ == "__main__":
    data = fetch_weather_for_cities()
    print(data)
