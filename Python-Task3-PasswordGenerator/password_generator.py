import secrets
import string
import tkinter as tk
from tkinter import messagebox

# Password Generator Function
def generate_password():
    try:
        length = int(length_var.get())  # get selected length from dropdown

        # Character sets
        letters = string.ascii_letters   # a-z + A-Z
        digits = string.digits           # 0-9
        symbols = string.punctuation     # !@#$%^&* etc.

        # Ensure password has at least one of each type
        password = [
            secrets.choice(letters),
            secrets.choice(digits),
            secrets.choice(symbols)
        ]

        # Fill the rest with random choices from all sets
        all_chars = letters + digits + symbols
        password += [secrets.choice(all_chars) for _ in range(length - 3)]

        # Shuffle to avoid predictable order
        secrets.SystemRandom().shuffle(password)

        # Join list into string
        final_password = "".join(password)

        # Show result
        entry_result.delete(0, tk.END)
        entry_result.insert(0, final_password)

        # Check strength
        strength = check_strength(final_password)
        label_strength.config(text=strength[0], fg=strength[1])

    except ValueError:
        messagebox.showerror("Error", "Please select a valid length.")

# Strength Checker
def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length < 6 or score < 2:
        return ("Easy / Risky", "red")
    elif 6 <= length < 10 and score >= 3:
        return ("Medium", "orange")
    else:
        return ("Strong", "green")

# Copy to Clipboard
def copy_password():
    password = entry_result.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("420x250")

# Length selection
tk.Label(root, text="Select Password Length:").pack(pady=5)
length_var = tk.StringVar(value="8")
length_dropdown = tk.OptionMenu(root, length_var, *[str(i) for i in range(6, 21)])
length_dropdown.pack(pady=5)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Result field
tk.Label(root, text="Generated Password:").pack(pady=5)
entry_result = tk.Entry(root, width=40)
entry_result.pack(pady=5)

# Strength label
label_strength = tk.Label(root, text="", font=("Arial", 12))
label_strength.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=10)

root.mainloop()


