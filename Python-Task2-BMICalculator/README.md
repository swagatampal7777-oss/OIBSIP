# ⚖️ BMI Calculator

## 📖 Project Overview
This project is an **BMI Calculator** built with Python.  
It provides a simple **GUI interface** for users to calculate their Body Mass Index (BMI) and track changes over time.  

### ✨ Key Features
- 👤 User name input for personalized tracking.
- 📅 Date field to record when BMI was calculated.
- ⚖️ Input **weight** in kilograms or pounds.
- Input **height** in meters, centimeters, or feet+inches.
- Input **date manually** (e.g., `2026-08-13`) to track BMI history.
- Stores BMI records in a local **SQLite database** (`bmi_records.db`).
- 📊 Displays BMI classification (Underweight, Normal, Overweight, Obese).
- 📈 Plots **BMI vs. Date** graph using Matplotlib for progress tracking.

---

## ⚙️ Dependencies
- **tkinter** → built-in with Python  
- **sqlite3** → built-in with Python  
- **matplotlib** → install with:
```bash
    pip install matplotlib
```

## 🚀 How to Run

  1. Clone the repository:
```bash
      git clone https://github.com/<your-username>/OIBSIP.git
      cd OIBSIP/Python-Task2-BMICalculator
```

  2. Run the app:
```bash
      python bmi_calculator.py
```
  3. Enter:
      ~ User name
      ~ Date (YYYY-MM-DD)
      ~ Weight + unit
      ~ Height + unit

         Then click Calculate → BMI result is shown and saved.
         Click Show Trend → view BMI vs Date graph.

## Expected Output

    Example BMI calculation:
      BMI: 22.5 (Normal)

    Example trend graph:
      X-axis → Date
      Y-axis → BMI values
      Line plot showing BMI changes over time

## 🗂️ Project Structure

    Python-Task2-BMICalculator/
      │── bmi_calculator.py   # Main Python script
      │── bmi_records.db      # SQLite database (auto-created)
      │── README.md           # Project documentation

## 🎯 Learning Outcomes
- Strengthened Git/GitHub workflow skills.
- Learned project structuring with README.md and documentation.
- Took reference from Copilot for Tkinter GUI, SQLite integration, and Matplotlib plotting.
- Gained confidence in organizing beginner Python projects.

## 📌 Future Improvements
- Add user authentication for BMI records.
- Export BMI records to CSV/Excel.
- Enhance GUI with modern themes.