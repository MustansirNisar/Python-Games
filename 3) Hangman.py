import random

def hangman():
    # List of words for the game
    words = ["python", "hangman", "javascript", "developer", "programming", "algorithm", "django", "flask", "github"]
    
    # Randomly choose a word from the list
    word_to_guess = random.choice(words)
    
    # Initialize the game state
    word_length = len(word_to_guess)
    guessed_word = ["_"] * word_length
    guessed_letters = set()
    attempts = 7
    
    # Hangman visual states
    hangman_stages = [
        """
         ------
         |    |
         |    
         |   
         |   
         |    
         |    
        ---
        """,
        """
         ------
         |    |
         |    O
         |   
         |   
         |    
         |    
        ---
        """,
        """
         ------
         |    |
         |    O
         |    |
         |   
         |    
         |    
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |   
         |    
         |    
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   
         |    
         |    
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / 
         |    
         |    
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |    
         |    
        ---
        """
    ]
    
    print("Welcome to Hangman!")
    print("Try to guess the word.")
    print(f"The word has {word_length} letters.")
    
    # Game loop
    while attempts > 0:
        print(hangman_stages[7 - attempts])  # Show the hangman based on attempts left
        print(f"Guessed Word: {' '.join(guessed_word)}")
        print(f"Used Letters: {', '.join(sorted(guessed_letters))}")
        print(f"Attempts left: {attempts}")
        
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue
        
        # Add the guess to the set of guessed letters
        guessed_letters.add(guess)
        
        # Check if the letter is in the word
        if guess in word_to_guess:
            print(f"Good guess! The letter '{guess}' is in the word.")
            # Update the guessed word
            for i in range(word_length):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            attempts -= 1
        
        # Check if the player has won
        if "_" not in guessed_word:
            print(f"Congratulations! You've guessed the word: {''.join(guessed_word)}")
            break
    else:
        print(f"Sorry, you've run out of attempts! The word was: {word_to_guess}")

# Call the game function to start the game
hangman()

