#Please guess who is the winner of the latest Pall Mall game
from IPython.display import clear_output

def run():
    print("Welcome to my interactive game!")

    username = input("What is your name? ")
    print(f"Hello, {username}! Let's start the game.")
    print("Please guess who is the winner of the latest Pall Mall game.")

    name_list = ["Violet", "Anthony", "Benedict", "Colin","Daphne", "Eloise", "Francesca", "Gregory", "Hyacinth"]

    print("Please choose one name from the list:")
    print(", ".join(name_list))

    while True:
        name = input("Your choice: ")

        if name not in name_list:
            print("❌ This name is not in the list. Please try again.")
            continue

        if name == "Anthony":
            print("🎉 Congratulations! You are correct!")
            break

        print("It's someone else. Guess again.")

        play_again = input("Do you want to try again? (yes / no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
