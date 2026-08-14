# Random Password Generator

## 📖 Project Overview
This project is a **Secure Random Password Generator** built with Python and Tkinter.  
Unlike traditional generators that use the `random` module, this project uses Python’s **`secrets`** module, which provides **cryptographically secure randomness**.  
It ensures that generated passwords are unpredictable and safe for real-world use.

### Key Features
- Select password length from a dropdown menu (6–20 characters).
- Generates passwords with letters, digits, and symbols.
- Ensures at least one uppercase, lowercase, digit, and symbol.
- Rates password strength:
  - **Easy / Risky** → Red text
  - **Medium** → Orange text
  - **Strong** → Green text
- Copy generated password to clipboard with one click.
- Secure randomness using `secrets` (CSPRNG).

---

##  Dependencies
This project uses only built-in Python libraries:
- **secrets** → cryptographically secure random generator  
- **string** → character sets (letters, digits, symbols)  
- **tkinter** → GUI interface  
 No external installation required.

---

##  How to Run on Your System
1. Clone the repository:
   
   git clone https://github.com/<your-username>/OIBSIP.git
   cd OIBSIP/Python-Task3-PasswordGenerator

2. Run the program:

    python password_generator.py

3. Steps in the GUI:

    ~ Select desired password length from dropdown.

    ~ Click Generate Password.

    ~ View generated password in the text box.

    ~ Check strength indicator (colored text).

    ~ Click Copy to Clipboard to copy password.

## Expected Output
    Example generated password:
        A7!bX9@qLm

    Strength indicator:
        Strong (Green)

## Project Structure

    Python-Task3-PasswordGenerator/
        │── password_generator.py   # Main Python script (uses secrets)
        │── README.md               # Project documentation

