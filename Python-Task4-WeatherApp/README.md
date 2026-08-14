# 🌤️ Advanced Weather Forecast App

## 📖 Project Overview
This project is a **Weather Forecast Application** built with Python, Tkinter, and the OpenWeatherMap API.  
It provides real-time weather information, hourly forecasts, and daily forecasts with a clean GUI interface.  
The app also supports **automatic location detection**, displays **weather icons**, and allows users to toggle between **Celsius and Fahrenheit**.

---

## Features
- Detects location automatically using **ipinfo.io** API.
- City input field for manual search.
- Displays current temperature, humidity, and condition.
- Shows weather icons corresponding to conditions.
- Hourly forecast (next 6 hours).
- Daily forecast (next 5 days).
- Unit toggle: Celsius ↔ Fahrenheit.
- Error messages shown inside GUI (not terminal).

---

## Dependencies
Install the required libraries:

    pip install requests pillow

## How to Run
    1. Clone the repository:
        git clone https://github.com/<your-username>/OIBSIP.git
        cd OIBSIP/Python-Task4-WeatherApp

    2. Replace the placeholder API key in the code:
        API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

    (Get your free API key from OpenWeatherMap)

    3. Run the app:
        python weather_app.py

    4. Enter a city name or leave blank (auto-detects location).
    Click Get Weather → view results, icons, hourly & daily forecast.

## Expected Output
    Example current weather:
        Kolkata
        Clear Sky
        Temperature: 30°C
        Humidity: 70%

    Example forecast:
        Hourly Forecast:
            2026-08-15 03:00:00: 29°C, Clear Sky
            2026-08-15 06:00:00: 28°C, Few Clouds

        Daily Forecast:
            2026-08-15: 30°C, Clear Sky
            2026-08-16: 31°C, Rain
...

## Project Structure

    Python-Task4-WeatherApp/
        │── weather_app.py     # Main Python script
        │── README.md          # Project documentation
