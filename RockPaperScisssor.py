import random

def play_rps():
    print("Welcome to Rock, Paper, Scissors game!")
    
    # Define the options
    options = ["rock", "paper", "scissors"]
    
    # Get user input
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    # Validate the user's input
    if user_choice not in options:
        print("Invalid choice, please choose rock, paper, or scissors.")
        return play_rps()  # Recursive call if invalid input
    
    # Get the computer's choice
    computer_choice = random.choice(options)
    print(f"The computer chose: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
    
    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        play_rps()  # Recursively call the function to play again
    else:
        print("Thanks for playing! Goodbye.")

# Call the function to start the game
play_rps()

