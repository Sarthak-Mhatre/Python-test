import random

# List of possible words for the game
words = ['python', 'javascript', 'java', 'kotlin', 'swift', 'golang', 'ruby', 'html', 'css']


def get_random_word():
    return random.choice(words).upper()


def display_current_state(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])


def hangman():
    word = get_random_word()  # Select a random word
    guessed_letters = set()  # Keep track of guessed letters
    incorrect_guesses = set()  # Keep track of incorrect guesses
    attempts = 6  # Number of attempts

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord:", display_current_state(word, guessed_letters))
        print(f"Incorrect guesses: {' '.join(incorrect_guesses)}")
        print(f"Remaining attempts: {attempts}")

        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.add(guess)
        else:
            print("Incorrect guess.")
            incorrect_guesses.add(guess)
            attempts -= 1

        # Check if the player has guessed the word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")


# Run the hangman game
if __name__ == '__main__':
    hangman()
