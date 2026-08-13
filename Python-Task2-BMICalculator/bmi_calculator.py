import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import matplotlib.pyplot as plt

# Database Setup
conn = sqlite3.connect("bmi_records.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS records (
        user TEXT,
        weight REAL,
        height REAL,
        bmi REAL,
        date TEXT
    )
""")
conn.commit()

# Helper Functions 
def convert_weight(value, unit):
    if unit == "kg":
        return value
    elif unit == "lbs":
        return value * 0.453592
    else:
        raise ValueError("Invalid weight unit")

def convert_height(value1, value2, unit):
    if unit == "m":
        return value1
    elif unit == "cm":
        return value1 / 100
    elif unit == "ft+in":
        return (value1 * 0.3048) + (value2 * 0.0254)
    else:
        raise ValueError("Invalid height unit")

# BMI Calculation
def calculate_bmi():
    try:
        user = entry_user.get().strip()
        date = entry_date.get().strip()
        weight = float(entry_weight.get())
        height1 = float(entry_height1.get())
        height2 = float(entry_height2.get()) if entry_height2.get() else 0

        if not user or not date:
            messagebox.showerror("Error", "Please enter both user name and date.")
            return

        weight_kg = convert_weight(weight, weight_unit.get())
        height_m = convert_height(height1, height2, height_unit.get())

        if weight_kg <= 0 or height_m <= 0:
            messagebox.showerror("Error", "Weight and height must be positive numbers.")
            return

        bmi = weight_kg / (height_m ** 2)

        if bmi < 18.5:
            category, color = "Underweight", "blue"
        elif 18.5 <= bmi < 25:
            category, color = "Normal", "green"
        elif 25 <= bmi < 30:
            category, color = "Overweight", "orange"
        else:
            category, color = "Obese", "red"

        label_result.config(text=f"BMI: {bmi:.2f} ({category})", foreground=color)

        # Save with user-input date
        cursor.execute("INSERT INTO records VALUES (?, ?, ?, ?, ?)", (user, weight_kg, height_m, bmi, date))
        conn.commit()

    except ValueError:
        messagebox.showerror("Error", "Please enter numeric values only.")

# Show Trend 
def show_trend():
    user = entry_user.get().strip()
    if not user:
        messagebox.showerror("Error", "Please enter a user name.")
        return

    cursor.execute("SELECT bmi, date FROM records WHERE user=?", (user,))
    data = cursor.fetchall()

    if data:
        bmis = [row[0] for row in data]
        dates = [row[1] for row in data]
        plt.plot(dates, bmis, marker="o", color="purple")
        plt.title(f"BMI Trend for {user}")
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showinfo("Info", "No records found for this user.")

# GUI Setup
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("520x350")
root.configure(bg="#f9f9f9")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10), padding=5)

# User Name
ttk.Label(root, text="User Name").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_user = ttk.Entry(root)
entry_user.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

# Date
ttk.Label(root, text="Date (YYYY-MM-DD)").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_date = ttk.Entry(root)
entry_date.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

# Weight
ttk.Label(root, text="Weight").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_weight = ttk.Entry(root, width=10)
entry_weight.grid(row=2, column=1, padx=5, pady=5)
weight_unit = ttk.Combobox(root, values=["kg", "lbs"], width=6, state="readonly")
weight_unit.set("kg")
weight_unit.grid(row=2, column=2, padx=5, pady=5)

# Height
ttk.Label(root, text="Height").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_height1 = ttk.Entry(root, width=10)
entry_height1.grid(row=3, column=1, padx=5, pady=5)
entry_height2 = ttk.Entry(root, width=10)
entry_height2.grid(row=3, column=2, padx=5, pady=5)
height_unit = ttk.Combobox(root, values=["m", "cm", "ft+in"], width=6, state="readonly")
height_unit.set("m")
height_unit.grid(row=3, column=3, padx=5, pady=5)

# Buttons
ttk.Button(root, text="Calculate", command=calculate_bmi).grid(row=4, column=0, padx=5, pady=10)
ttk.Button(root, text="Show Trend", command=show_trend).grid(row=4, column=1, padx=5, pady=10)

# Result Label
label_result = ttk.Label(root, text="", font=("Arial", 12))
label_result.grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()

