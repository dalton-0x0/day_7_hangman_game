# hangman game
import random

from hangman_art import logo, stages
from hangman_words import word_list

# intialize
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

# create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # if user has enters already guessed letter, print it and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # check if user is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # join all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")

    # check if user has got all letters of the word
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
