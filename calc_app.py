import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight_text = weight_entry.get().strip()
        height_text = height_entry.get().strip()

        # Ensure input is not empty
        if not weight_text or not height_text:
            messagebox.showerror("Input Error", "Please enter both weight and height.")
            return

        weight = float(weight_text)
        height = float(height_text)

        # Ensure height is not zero
        if height <= 0:
            messagebox.showerror("Input Error", "Height must be greater than zero.")
            return

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")

# Create main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

# Labels & Entry Fields
tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

# Calculate Button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="BMI: \nCategory:")
result_label.pack(pady=10)

# Run the app
root.mainloop()
