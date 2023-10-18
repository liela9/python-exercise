import random
import re

WORDS = ["hang", "translate", "apple","orange", "length", "right", "table", "name", "word", "palindrom"]
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

count_mistakes = 0

# Lose organ when the user wrong
def mistake():
    global count_mistakes
    count_mistakes += 1
    print(HANGMANPICS[count_mistakes - 1])

    if count_mistakes == len(HANGMANPICS):
        print("YOU LOSE!")
        exit()


word_to_guess = random.choice(WORDS)
word_to_print = []

# Fill the word that presents to the user with '_'
# Example: for the word "night" it will be "_ _ _ _ _"
for _ in word_to_guess:
    word_to_print.append('_')

end_of_game = False

# Logic of the game
# Play while there are letters left to guess
while not end_of_game:
    print(f"{''.join(word_to_print)}")
    letter = input("Please guess a letter: ").lower()

    if letter in word_to_guess:
        # If the user already guessed that letter, than lose organ
        if letter in word_to_print:
            print("You have already guessed that letter")
            mistake()
            continue

        # Find the indexes of the occurences
        occurences = [i.start() for i in re.finditer(letter, word_to_guess)]
        # Fill the letter in the correct places
        for j in occurences:
            word_to_print[j] = letter
            
        # If the user guessed all the letters correctly, than they win
        if '_' not in word_to_print:
            print(f"{''.join(word_to_print)}")
            print("YOU WON ! !")
            end_of_game = True
    else:
        mistake()
    