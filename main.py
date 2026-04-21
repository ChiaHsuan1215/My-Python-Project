def guess_name():
   print("Welcome to my interactive game!")

   username = input("What is your name? ")
   print(f"Hello, {username}! Let's start the game.")
   print('Please guess who is the winner of the latest Pall Mall game.')

from IPython.display import clear_output()

# List of valid names
name_list = [ 'Violet', 'Anthony', 'Benedict', 'Colin', 'Daphne', 'Eloise', 'Francesca', 'Gregory', 'Hyacinth']

    print("Please choose one name from the list:")
    print(", ".join(name_list))

    while True:
        name = input("Your choice: ")

        # Name not in list
        if name not in name_list:
            print("This name is not in the list. Please try again.")
            continue

        # Correct answer
        if name == 'Anthony':
            print("Congratulations! You are correct!")
            break

        # Wrong but valid name
        print("It's someone else. Guess again.")


def ask_play_again():
    while True:
        choice = input("\nDo you want to play again? (Yes / No): ").strip().lower()

        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print(" Please enter 'Yes' or 'No'.")


# Main game loop
while True:
    guess_name()

    if not ask_play_again():
        print("\n Thanks for playing! See you next time.")
        break

     
     
    
       
     
   
