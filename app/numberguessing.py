# number_guessing_game.py

import random

def number_guessing_game():
    print("🎯 Welcome to Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (or 0 to quit): "))
        except ValueError:
            print(" Please enter a valid number.")
            continue

        if guess == 0:
            print("You quit the game. Goodbye!")
            break

        attempts += 1

        if guess < number:
            print(" Too low! Try again.")
        elif guess > number:
            print(" Too high! Try again.")
        else:
            print(f" Correct! You guessed it in {attempts} attempts!")
            break

if __name__ == "__main__":
    number_guessing_game()
