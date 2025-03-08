import random

def guess(x):
    random_number = random.randint(1, x)
    attempts = 0
    max_attempts = 5  # You can adjust the maximum attempts here.
    
    print(f"Welcome to the number guessing game! Try to guess the number between 1 and {x}. You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: Guess a number between 1 and {x}: ")
        
        # Input validation: check if the input is a number and within range
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        
        if guess < 1 or guess > x:
            print(f"Your guess must be between 1 and {x}. Please try again.")
            continue
        
        attempts += 1
        
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
        else:
            print(f"Yay! Congrats. You've guessed the number {random_number} correctly in {attempts} attempts.")
            break
    else:
        print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {random_number}. Better luck next time!")

guess(10)

