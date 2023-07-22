import random

def select_random_word():
    """Selects a random word from a list of words"""
    words = ["computer", "programming", "hangman", "python", "game"]
    return random.choice(words)

def update_word(word, guessed_letters):
    """Updates the word to reveal correctly guessed letters"""
    updated_word = ""
    for letter in word:
        if letter in guessed_letters:
            updated_word += letter + " "
        else:
            updated_word += "_ "
    return updated_word.strip()

def hangman():
    print("Welcome to Hangman!")

    word = select_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    while True:
        print("\nAttempts left:", max_attempts - incorrect_guesses)
        print("Word:", update_word(word, guessed_letters))

        if "_" not in update_word(word, guessed_letters):
            print("\nCongratulations! You guessed the word correctly!")
            break

        if incorrect_guesses == max_attempts:
            print("\nGame over! You ran out of attempts. The word was", word)
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess in word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Wrong guess!")
                incorrect_guesses += 1
        else:
            print("Invalid input. Please enter a single letter.")

# Run the game
hangman()
