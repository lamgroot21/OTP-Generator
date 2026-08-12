import random
def generate_otp():
    return random.randint(1000,9999)

otp = generate_otp()
print("Your otp is:",otp)

user_otp = int(input("Enter the OTP: "))

if user_otp == otp:
    print("OTP verified successfully!")
else:
    print("Invalid OTP. Please try again.")