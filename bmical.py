import tkinter as tk
from tkinter import messagebox
import os

# Text file to store BMI data
DATA_FILE = "bmi_history.txt"

# Function to calculate BMI
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

# Classify BMI into category
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Save data to text file
def save_data(username, bmi):
    with open(DATA_FILE, "a") as file:
        file.write(f"{username},{bmi}\n")

# Show history as simple text (no graph)
def show_history(username):
    if not os.path.exists(DATA_FILE):
        messagebox.showinfo("Info", "No BMI records found.")
        return

    records = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            name, bmi = line.strip().split(",")
            if name == username:
                records.append(bmi)

    if records:
        history = "\n".join([f"{i+1}) BMI: {b}" for i, b in enumerate(records)])
        messagebox.showinfo("BMI History", f"BMI records for {username}:\n\n{history}")
    else:
        messagebox.showinfo("No Data", f"No records found for {username}.")

# Main BMI calculation logic
def calculate_and_display():
    try:
        username = username_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not username:
            messagebox.showerror("Input Error", "Please enter your name.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        result_label.config(text=f"BMI: {bmi} ({category})")
        save_data(username, bmi)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

# ---------------------------
# GUI Setup using Tkinter
# ---------------------------
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Height (m):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Calculate BMI", command=calculate_and_display).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(root, text="View History", command=lambda: show_history(username_entry.get().strip())).grid(row=4, column=0, columnspan=2)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
