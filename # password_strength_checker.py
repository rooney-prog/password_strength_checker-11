# password_strength_checker.py

import re

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1

    return strength

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    score = check_password_strength(password)

    if score <= 2:
        print("Weak password 🔴")
    elif score == 3 or score == 4:
        print("Moderate password 🟡")
    else:
        print("Strong password 🟢")

if __name__ == "__main__":
    main()
