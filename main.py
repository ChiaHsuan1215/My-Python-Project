from IPython.display import clear_output()

def guess_name():
   print("Welcome to my interactive game!")

   username = input("What is your name? ")
   print(f"Hello, {username}! Let's start the game.")
   print('Please guess who is the winner of the latest Pall Mall game.')


   # List of valid names
   name_list = ['Violet', 'Anthony', 'Benedict', 'Colin','Daphne', 'Eloise', 'Francesca', 'Gregory', 'Hyacinth']

   print("Please choose one name from the list:")
   print(", ".join(name_list))

   while True:
        name = input("Your choice: ")

        # Case 1: Name not in list
        if name not in name_list:
            print("❌ This name is not in the list. Please try again.")
            continue

        # Case 2: Correct answer
        if name == 'Anthony':
            print("Congratulations! You are correct!")
            break

        # Case 3: Wrong but valid name
        print(" It's someone else. Guess again.")

        play_again = input("Do you want to try again? (Yes / No): ").strip().lower()

        if play_again == "yes":
            continue     
        else:
            print(" Thanks for playing!")
            break         


# Run game
guess_name()

     
     
    
       
     
   
