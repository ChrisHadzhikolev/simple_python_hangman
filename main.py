import random as rand
import word_list
import ascii_art

print(ascii_art.logo)
chosen_word = rand.choice(word_list.word_list)

lives = 6
display = []
for letter in chosen_word:
    display.append('_')

print(f"{' '.join(display)}")

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
            print(ascii_art.stages[lives])
            break
    print(f"{' '.join(display)}")
if lives == 0:
    print('You Lose!')
else:
    print('You Win!')
