import random

def play_hangman():
    """Plays a game of hangman, following the steps in the image."""

    # Word Selection: Choose a random word from a predefined list.
    word_list = ["python", "hangman", "programming", "computer", "challenge", "developer"]
    secret_word = random.choice(word_list).upper()
    
    # Game Setup: Initialize variables.
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6
    
    # Game Loop: Keeps the game running.
    while True:
        # Display Interface: Show hangman figure and partially revealed word.
        display_hangman(incorrect_guesses)
        display_word(secret_word, guessed_letters)
        
        # Win/Loss Conditions: Check for a win before user input.
        if all(letter in guessed_letters for letter in secret_word):
            print("\n🎉 Congratulations! You guessed the word correctly!")
            break
            
        # User Input: Prompt for a letter and validate.
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)
        
        # Check Guess: Validate the letter and update the game.
        if guess not in secret_word:
            incorrect_guesses += 1
            print(f"\n❌ Sorry, '{guess}' is not in the word.")
            if incorrect_guesses >= max_attempts:
                display_hangman(incorrect_guesses)
                print(f"\n😢 Game over! The word was '{secret_word}'.")
                break
        else:
            print(f"\n✅ Good guess! '{guess}' is in the word.")

    # Play Again: Offer the option to restart.
    play_again_option()

def display_hangman(incorrect_guesses):
    """Displays the hangman figure based on incorrect guesses."""
    stages = [  # These represent the different stages of the hangman figure.
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ---------
        """
    ]
    print(stages[incorrect_guesses])

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("\n" + display)

def get_guess(guessed_letters):
    """Prompts the user for a letter and validates the input."""
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("❗ Invalid input. Please enter a single letter.")
        elif guess in guessed_letters:
            print("🚫 You've already guessed that letter. Try a new one.")
        else:
            return guess

def play_again_option():
    """Asks the player if they want to play again."""
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice in ['yes', 'y']:
            print("\nStarting a new game...")
            play_hangman()
            break
        elif choice in ['no', 'n']:
            print("Thanks for playing! 👋")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "_main_":
    play_hangman()