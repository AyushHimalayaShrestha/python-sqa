# password_generator.py

import random
import string

def generate_password(length=12):
    """Generate a random password with letters, digits, and symbols"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Random Password Generator")
    
    while True:
        try:
            length = int(input("Enter password length (default 12, type 0 to exit): "))
            if length == 0:
                print(" Goodbye!")
                break
            elif length < 6:
                print(" Password too short! Minimum length is 6.")
            else:
                print("Generated Password:", generate_password(length))
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
