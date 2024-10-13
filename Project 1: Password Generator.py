# Build a simple password generator that uses string concatenation and random selections of letters.
import string
import random

lowercase = string.ascii_lowercase # # Create a pool of characters (lowercase, uppercase, digits, symbols)  
uppercase = string.ascii_uppercase
digits = string.digits
punctuations = ['!', '@', '#', '$', '%', '^', '&', '*']


## choose random characters 
password_characters = random.choice(lowercase) + random.choice(uppercase) + random.choice(digits) + random.choice(punctuations)

#combine and shuffle
password = ''.join(random.choices(password_characters, k=10))

print(password)

first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()

print (f"{first_name} {last_name}")