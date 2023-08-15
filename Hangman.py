import random

def load_words_from_file(file_path):
    with open('hangman_word_list.txt', 'r') as file:
        words = file.read().splitlines()
    return words

words = load_words_from_file('hangman_word_list.txt')

chosen_word = random.choice(words)


def replay_game():
    replay = input("Do you want to play again? (yes/no): ").lower()
    return replay == 'yes'

def display(word, guessed_letters, attempts):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)
    print(f"Attempts remaining: {attempts}")

def hangman():
    words = load_words_from_file('hangman_word_list.txt')

    replay = True

    while replay:
        chosen_word = random.choice(words)
        guessed_letters = []
        attempts = 6

        print()
        print("Welcome to Hangman! Can you guess the word in only 6 guesses?")

        while attempts > 0:
            display(chosen_word, guessed_letters, attempts)

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter")
                continue

            if guess in guessed_letters:
                print("You've already guessed that letter")
                continue

            guessed_letters.append(guess)

            if guess in chosen_word:
                print("Correct!")
                if chosen_word == ''.join([letter if letter in guessed_letters else '_' for letter in chosen_word]):
                    print()
                    print(f"Congratulations! The word was {chosen_word}. You did it!")
                    break
            else:
                print("Incorrect guess.")
                attempts -= 1

        while attempts == 0:
            print()
            print(f"The word was {chosen_word}. Better luck next time!")
            break

        replay = replay_game()

    print("Thanks for playing Hangman!")


hangman()