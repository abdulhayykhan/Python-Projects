import tkinter as tk
from tkinter import messagebox
import re
import random
import string

def check_password_strength(password):
    strength = 0
    suggestions = []
    
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Make your password at least 8 characters long.")
    
    if any(char.isupper() for char in password):
        strength += 1
    else:
        suggestions.append("Include at least one uppercase letter.")
    
    if any(char.islower() for char in password):
        strength += 1
    else:
        suggestions.append("Include at least one lowercase letter.")
    
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        suggestions.append("Include at least one number.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&* etc.).")
    
    common_passwords = ["123456", "password", "12345678", "qwerty", "abc123"]
    if password in common_passwords:
        strength = 1
        suggestions.append("Your password is too common. Choose a more unique one.")
    
    return strength, suggestions

def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(16))

def analyze_password():
    password = entry.get()
    strength, suggestions = check_password_strength(password)
    
    if strength == 5:
        messagebox.showinfo("Password Strength", "Your password is strong!")
    else:
        messagebox.showwarning("Weak Password", "Your password could be stronger:\n\n" + "\n".join(suggestions))

def suggest_password():
    strong_password = generate_password()
    entry.delete(0, tk.END)
    entry.insert(0, strong_password)
    messagebox.showinfo("Suggested Password", f"Try using this strong password:\n{strong_password}")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def clear_fields():
    entry.delete(0, tk.END)
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x300")

label = tk.Label(root, text="Enter your password:")
label.pack(pady=5)

entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=analyze_password)
check_button.pack(pady=5)

suggest_button = tk.Button(root, text="Suggest Strong Password", command=suggest_password)
suggest_button.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.pack(pady=5)

root.mainloop()
