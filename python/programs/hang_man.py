import random


def display_hangman(stage):
    hangman_art = {
        0: """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        1: """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        2: """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        3: """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        4: """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        5: """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        6: """
           -----
           |   |
           O   |
          /|\\  |
          / \\\  |
               |
        =========
        """,
    }
    print(hangman_art[stage])


def choose_word():
    word_list = [
        {"word": "python", "hint": "A popular programming language"},
        {"word": "apple", "hint": "A fruit and a tech company"},
        {"word": "guitar", "hint": "A musical instrument with strings"},
        {"word": "ocean", "hint": "A large body of water"},
        {"word": "mountain", "hint": "A natural elevation of the earth's surface"},
    ]
    random.seed()  # Ensure randomness
    return random.choice(word_list)


def play_game():
    chosen = choose_word()
    word = chosen["word"].lower()
    hint = chosen["hint"]

    guessed = set()
    wrong_guesses = 0
    max_attempts = 6
    display_word = ["_" for _ in word]

    print("Welcome to Hangman!")
    print("Hint:", hint)

    while wrong_guesses < max_attempts:
        print("\nCurrent word:", " ".join(display_word))
        display_hangman(wrong_guesses)
        guess = input("Enter a letter (or type 'hint' for a hint): ").lower()

        if guess == "hint":
            print("Hint:", hint)
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter!")
            continue

        guessed.add(guess)

        if guess in word:
            print(f"Good job! {guess} is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
        else:
            print(f"Oops! {guess} is not in the word.")
            wrong_guesses += 1

        if "_" not in display_word:
            print("\nCongratulations! You guessed the word:", word)
            break

    if wrong_guesses == max_attempts:
        display_hangman(wrong_guesses)
        print("\nGame Over! The word was:", word)


def main():
    play_game()


if __name__ == "__main__":
    main()
