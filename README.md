# Real-Time Weather Monitoring System
# Table of Contents
1. Overview
2. Features
3. Technologies Used
4. Setup Instructions
5. API Endpoints
6. Running the Application
7. Testing
# Overview
The Real-Time Weather Monitoring System is a web application that continuously retrieves and processes weather data from the OpenWeatherMap API. The system provides real-time insights, daily weather summaries, and alert notifications based on user-defined thresholds. The front end allows users to search for a city and view the weather summary, including temperature and dominant weather conditions. (https://openweathermap.org/)

the website is hosted: [file:///C:/Users/Shivani%20Reddy/Desktop/Weather%20Monitoring/frontend/index.html](url)
# Features
1. Real-time weather data retrieval for multiple cities in India.
2. Daily weather summaries including average, maximum, and minimum temperatures.
3. User-configurable alert thresholds for temperature conditions.
4. Search functionality to retrieve weather data for a specific city.
5. Visual representation of weather data and alerts.
# Technologies Used
# Frontend:
1. HTML
2. CSS
3. JavaScript
# Backend:
1. Python
2. Flask
# Database (if implemented):
1. SQLite or any other preferred database for storing daily summaries
# API:
1. OpenWeatherMap API
# Setup Instructions
# Prerequisites
1. Python 3.x
2. A free account on OpenWeatherMap to obtain an API key.
# Clone the Repository  
``` git clone https://github.com/yourusername/weather-monitoring-system.git
cd weather-monitoring-system
```
# Install Backend Dependencies
1. **Create a virtual environment (optional but recommended):**
``` python -m venv venv
source venv/scripts/activate  # On Windows use `venv\Scripts\activate`
```
2. **Install Flask :**
```pip install Flask
```
# Create a .env File
1. **Create a file named .env in the root directory.**
2. **Add your OpenWeatherMap API key**
```API_KEY=your_openweathermap_api_key
```
# API Endpoints
 **1. GET /api/weather-summary**
 
**Description:** Retrieves the daily weather summary for a specified city or all cities.

**Query Parameters:**
 **.** city (optional): Name of the city to retrieve weather data for.
 
**Response:** JSON array containing weather summaries.

2. **GET /api/alerts**
   
 **Description:** Retrieves current weather alerts based on predefined thresholds.
# Testing
1. The application should be tested to ensure that:
   It correctly retrieves and displays weather data.

   The alerts are triggered based on the specified conditions.

   The search functionality returns accurate results.
2. Manual testing can be performed by interacting with the front end and monitoring the backend responses.

# Website Out Come 

![Screenshot (70)7](https://github.com/user-attachments/assets/08445767-52de-4e69-906a-12f787fe2671)


