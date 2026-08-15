# 🖥️ OIBSIP Internship Projects (Python Track)

## 📖 Overview
This repository contains the Python projects developed during the **Oasis Infobyte Internship (OIBSIP)**.  
Each project demonstrates practical applications of Python programming, GUI development, API integration, and database handling.  

Projects included:
1. ⚖️ **BMI Calculator**
2. 🔐 **Random Password Generator**
3. 🌤️ **Basic Weather App**

---

## ✨ Projects

### 1. ⚖️ BMI Calculator
- Calculates Body Mass Index (BMI) with multiple unit support (kg/lbs, m/cm/ft+in).
- Categorizes BMI into Underweight, Normal, Overweight, Obese.
- Stores records in a local SQLite database (`bmi_records.db`).
- Visualizes BMI trends over time using Matplotlib.

**Run:**
```bash
    cd Python-Task2-BMICalculator
    python bmi_calculator.py
```

### 2. 🔐 Random Password Generator
- Generates strong random passwords with letters, digits, and symbols
- Minimum length validation (default: 8 characters).
- Advanced version includes GUI, clipboard copy, and secure random generation.

**Run:**
```bash
    cd Python-Task3-PasswordGenerator
    python password_generator.py
```

### 3. 🌤️ Basic Weather App
- Fetches real-time weather data using the OpenWeatherMap API.
- Displays temperature, humidity, condition, and weather icons.
- Provides hourly forecast (next 6 hours) and daily forecast (next 5 days).
- Supports Celsius ↔ Fahrenheit toggle and auto-location detection.

**Run:**
```bash
    cd Python-Task4-WeatherApp
    python weather_app.py
```

## ⚙️ Dependencies
Install required libraries before running:
```bash
    pip install requests pillow matplotlib
```
👉 tkinter and sqlite3 are included with Python.

## 🗂️ Project Structure
```code
OIBSIP/
│── Python-Task2-BMICalculator/
│   ├── bmi_calculator.py
│   ├── bmi_records.db
│   └── README.md
│
│── Python-Task3-PasswordGenerator/
│   ├── password_generator.py
│   └── README.md
│
│── Python-Task4-WeatherApp/
│   ├── weather_app.py
│   └── README.md
│
└── README.md   # Main repository documentation
```

## 🎯 Learning Outcomes
- Strengthened understanding of Git and GitHub workflows (creating repositories, committing, pushing, organizing project folders).
- Learned how to structure projects with README.md files, screenshots, and clear documentation.
- Took reference from Copilot for guidance on:
- Tkinter (GUI basics)
- API integration (OpenWeatherMap, ipinfo.io)
- SQLite database usage
- Matplotlib for data visualization
- Requests & Pillow for API calls and image handling
- Gained confidence in managing beginner‑level Python projects and organizing them professionally.
- Learned small but important details like error handling, project structure, and writing clean commit messages.

## 📌 Future Improvements
- Add user authentication for BMI records.
- Enhance password generator with strength meter.
- Improve Weather App UI with modern themes.
- Package projects into standalone executables.