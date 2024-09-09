import random
WORD_LIST = ["python", "hangman", "challenge", "programming", "development"]
def select_random_word(word_list):
    """Randomly select a word from the list."""
    return random.choice(word_list)
def display_current_state(word, guessed_letters):
    """Display the current state of the guessed word."""
    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(f"Current word: {displayed_word}")
def display_guessed_letters(guessed_letters):
    """Display the letters guessed so far."""
    print(f"Guessed letters: {', '.join(guessed_letters)}")
def hangman_game():
    print("Welcome to the Hangman Challenge!")
    word_to_guess = select_random_word(WORD_LIST)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  
    print(f"Hint: The word has {len(word_to_guess)} letters.")
    while incorrect_guesses < max_incorrect_guesses:
        display_current_state(word_to_guess, guessed_letters)
        display_guessed_letters(guessed_letters)
        print(f"Remaining incorrect guesses: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You have already guessed that letter. Try a different one.")
            continue
        guessed_letters.add(guess)
        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"Congratulations! You guessed the word: '{word_to_guess}'")
                break
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")
    if incorrect_guesses == max_incorrect_guesses:
        print(f"Sorry, you've run out of guesses. The word was: '{word_to_guess}'")

if __name__ == "__main__":
    hangman_game()
