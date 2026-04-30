
from games.guess_name import run as guess_name_game
from games.number_guess import run as number_guess_game

def main():
    print("🎮 Welcome to My Python Games")
    print("1. Name Guessing Game")
    print("2. Number Guessing Game")

    choice = input("Choose a game (1 or 2): ")

    if choice == "1":
        guess_name_game()
    elif choice == "2":
        number_guess_game()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

     
     
    
       
     
   
