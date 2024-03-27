import tkinter as tk
from tkinter import messagebox
import random

# Function to generate a 6-digit OTP
def generate_otp():
    otp = ''.join(str(random.randint(0, 9)) for _ in range(6))
    return otp

# Function to verify OTP
def verify():
    entered_otp = otp_entry.get()
    generated_otp = otp_label.cget("text")

    try:
        if len(entered_otp) != 6 or not entered_otp.isdigit():
            raise ValueError("Please enter a valid 6-digit OTP.")

        if entered_otp == generated_otp:
            messagebox.showinfo("Success", "OTP verified successfully! Access granted.")
            root.destroy()
        else:
            messagebox.showerror("Error", "Incorrect OTP. Please try again.")
    except ValueError as e:
        messagebox.showerror("Error", e)

# Create GUI window
root = tk.Tk()
root.title("OTP Verification")

# Generate OTP
otp = generate_otp()

# Label to display OTP
otp_label = tk.Label(root, text=otp, font=("Arial", 24))
otp_label.pack(pady=10)

# Entry for user to input OTP
otp_entry = tk.Entry(root, font=("Arial", 18))
otp_entry.pack(pady=5)

# Button to verify OTP
verify_button = tk.Button(root, text="Verify OTP", command=verify)
verify_button.pack(pady=5)

# Run the GUI
root.mainloop()
