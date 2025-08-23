import random
words = ['hangmangame', 'pandas', 'Shadowfox', 'programming', 'python' , 'development' , 'challenge','internet']
word = random.choice(words)
guessed = []
tries = 6

print("Welcome to Hangman!")

while tries > 0:
    display = ''
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += '_'
    print(display)

    if '_' not in display:
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print("You already guessed that letter.")
    elif guess in word:
        print("Good guess!")
        guessed.append(guess)
    else:
        print("Wrong guess!")
        tries -= 1
        guessed.append(guess)
        print(f"Tries left: {tries}")

if '_' in display:
    print(f"Game Over! The word was {word}")