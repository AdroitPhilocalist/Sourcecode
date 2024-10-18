import random
import string

def generate_password(length):
    # Define characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Ask the user for desired password length
length = int(input("Enter the desired password length: "))
print(f"Your random password is: {generate_password(length)}")
