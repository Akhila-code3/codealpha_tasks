import random

# List of predefined words
words = ["python", "computer", "program", "keyboard", "monitor"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")

while incorrect_guesses < max_guesses:
    # Display the current progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Remaining incorrect guesses:", max_guesses - incorrect_guesses)

# If the player loses
if incorrect_guesses == max_guesses:
    print("\nGame Over! You ran out of guesses.")
    print("The word was:", word)