import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

# API Key
API_KEY = "66f3ca24dfc518d8f56c22413498d537"

# Helper Functions
def get_location():
    """Detect user's city using IP address via ipinfo.io"""
    try:
        ip_response = requests.get("https://ipinfo.io/json")
        ip_data = ip_response.json()
        return ip_data.get("city", "")
    except:
        return ""

def get_weather():
    city = entry_city.get()
    if not city:
        city = get_location()
        if not city:
            messagebox.showerror("Error", "Please enter a city name.")
            return

    unit = unit_var.get()  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={unit}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        # Extract weather details
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].capitalize()
        icon_code = data["weather"][0]["icon"]

        # Display results
        label_result.config(
            text=f"Temperature: {temp}°{'C' if unit=='metric' else 'F'}\n"
                 f"Humidity: {humidity}%\nCondition: {description}"
        )

        # Fetch and display icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        icon_img = Image.open(io.BytesIO(icon_response.content))
        icon_photo = ImageTk.PhotoImage(icon_img)
        label_icon.config(image=icon_photo)
        label_icon.image = icon_photo

        # Get forecast
        get_forecast(city, unit)

    except Exception as e:
        messagebox.showerror("Error", f"Unable to fetch weather data.\n{e}")

def get_forecast(city, unit):
    """Fetch 5-day / 3-hour forecast"""
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={unit}"
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "200":
            return

        # Next 6 hours (2 entries, since forecast is every 3 hours)
        hourly_text = "Hourly Forecast:\n"
        for i in range(2):
            forecast = data["list"][i]
            time = forecast["dt_txt"]
            temp = forecast["main"]["temp"]
            desc = forecast["weather"][0]["description"].capitalize()
            hourly_text += f"{time}: {temp}°{'C' if unit=='metric' else 'F'}, {desc}\n"

        label_hourly.config(text=hourly_text)

        # Next 5 days (pick one forecast per day)
        daily_text = "Daily Forecast:\n"
        for i in range(0, 40, 8):  # 8 entries per day
            forecast = data["list"][i]
            date = forecast["dt_txt"].split()[0]
            temp = forecast["main"]["temp"]
            desc = forecast["weather"][0]["description"].capitalize()
            daily_text += f"{date}: {temp}°{'C' if unit=='metric' else 'F'}, {desc}\n"

        label_daily.config(text=daily_text)

    except Exception as e:
        messagebox.showerror("Error", f"Unable to fetch forecast data.\n{e}")

# GUI Setup
root = tk.Tk()
root.title("Advanced Weather App")
root.geometry("500x600")

# Heading
tk.Label(root, text="🌤️ WEATHER FORECAST 🌤️", font=("Segoe UI", 20, "bold"), fg="#00bfff").pack(pady=10)

# City input
tk.Label(root, text="Enter City Name:").pack(pady=5)
entry_city = tk.Entry(root, width=30)
entry_city.pack(pady=5)

# Unit toggle
unit_var = tk.StringVar(value="metric")
tk.Radiobutton(root, text="Celsius", variable=unit_var, value="metric").pack()
tk.Radiobutton(root, text="Fahrenheit", variable=unit_var, value="imperial").pack()

# Button
tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

# Weather icon
label_icon = tk.Label(root)
label_icon.pack(pady=10)

# Hourly forecast
label_hourly = tk.Label(root, text="", font=("Arial", 10), justify="left")
label_hourly.pack(pady=10)

# Daily forecast
label_daily = tk.Label(root, text="", font=("Arial", 10), justify="left")
label_daily.pack(pady=10)

root.mainloop()
