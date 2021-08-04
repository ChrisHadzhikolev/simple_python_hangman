import random as rand

word_list = ["aardvark", "baboon", "camel", "wolf", "ginger", "zombie"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = rand.choice(word_list)
print(chosen_word)


display = []
for letter in chosen_word:
    display.append('_')

print(display)
# chosen_word_chars = list(set(chosen_word))

lives = 6

while '_' in display and lives > 0:
    guess = input('Enter a Letter: ')
    guess.lower()
    for i in range(len(chosen_word)):
        if guess in chosen_word:
            letter = chosen_word[i]
            if letter == guess:
                display[i] = letter
        else:
            lives -= 1
            print(stages[lives])
            break
    print(f"{' '.join(display)}")
if lives == 0:
    print('You Lose!')
else:
    print('You Win!')

