                                   # OTP Verification System

#Created by Naman Maheshwari (S7315)

'''Developing an OTP (One-Time Password) verification system.
The system should generate a 6-digit OTP and send it to the user's email address for verification.
Upon receiving the OTP, the user should enter it into the system for validation.
If the entered OTP matches the generated OTP, access should be granted; otherwise, access should be denied.'''

import random  #importing random

# Function to generate a 6-digit OTP
def generate_otp():
    otp = ''.join(str(random.randint(0,9)) for _ in range(6))
    return otp

# Function to send OTP to user's email
def verify_otp(generated_otp):
    print(f"\nEmail sent for OTP verification: {generated_otp}")  #define a function to display
    entered_otp = input("Enter the OTP: ")      #ask fot the input
    if len(entered_otp) != 6 or not entered_otp.isdigit():    #verify the otp
        raise ValueError("Please enter a valid 6-digit OTP.")
    return generated_otp == entered_otp   #Core part of the code - checks the entered otp and generated otp

def main():
    max_attempts = 3   #maximum attempts
    for _ in range(max_attempts):  #Loop for maximum attempts
        generated_otp = generate_otp()  # Generate new OTP for each attempt
        try:
            if verify_otp(generated_otp):
                print("OTP verified successfully! Access granted.")
                break  #Exit the loop on successful verification
            else:
                print("Incorrect OTP. Please try again.")
        except ValueError as e:
            print(e)
    else: #executes if all attempts fail,this else is connected to for loop
        print("Maximum attempts exceeded. Please try again later.")

if __name__ == "__main__": #This makes the code to start running from here
    main()
