import random

# Hangman stages (drawing)
HANGMAN_PICS = [
    """
      +---+
          |
          |
          |
         ===
    """,
    """
      +---+
      O   |
          |
          |
         ===
    """,
    """
      +---+
      O   |
      |   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|   |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
     /    |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
     / \\  |
         ===
    """
]

# Word list
WORDS = ["python", "development", "shadowfox", "hangman", "programming", "difficulty", "challenge", "variable", "function", "condition"]

def get_random_word():
    return random.choice(WORDS)

def display_game_state(word, guessed_letters, incorrect_guesses):
    print(HANGMAN_PICS[incorrect_guesses])
    
    # Show word with underscores for unguessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word.strip())
    print("Guessed Letters:", " ".join(sorted(guessed_letters)))
    print(f"Incorrect Guesses: {incorrect_guesses}/{len(HANGMAN_PICS)-1}\n")

def play_game():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("🎮 Welcome to Hangman!")
    print("Guess the word, letter by letter.\n")

    while incorrect_guesses < max_attempts:
        display_game_state(word, guessed_letters, incorrect_guesses)
        
        guess = input("Enter a letter: ").lower()

        # Validate input
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Invalid input. Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print("⚠ You already guessed that letter!\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!\n")
        else:
            print("❌ Wrong guess!\n")
            incorrect_guesses += 1

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            display_game_state(word, guessed_letters, incorrect_guesses)
            print("🎉 Congratulations! You guessed the word correctly!")
            break
    else:
        display_game_state(word, guessed_letters, incorrect_guesses)
        print(f"💀 You lost! The word was: {word}")

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for playing Hangman! Goodbye!")
            break

if _name_ == "_main_":
    main()