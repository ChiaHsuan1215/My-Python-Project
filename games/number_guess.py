# Practice project in online course
import random

#create a try/except function in case the user did not eneter a valid number
def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def run():
    print("Welcome to the Number Guessing Game!")

    correct_number = random.randint(1, 100)
    guess_count = 1
    guess = get_valid_number("Please choose a number from 1 to 100: ")

    while guess != correct_number:
        guess_count += 1

        if guess < correct_number:
            guess = get_valid_number("The correct number is larger. Please guess again: ")
        else:
            guess = get_valid_number("The correct number is smaller. Please guess again: ")

    print(f"Congratulations! The right number is {correct_number}. "
          f"It took you {guess_count} guesses.")


