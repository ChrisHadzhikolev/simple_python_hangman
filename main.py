import random as rand

word_list = ["aardvark", "baboon", "camel", "wolf", "ginger", "zombie"]

chosen_word = rand.choice(word_list)
print(chosen_word)


display = []
for letter in chosen_word:
    display.append('_')

print(display)
# chosen_word_chars = list(set(chosen_word))

while '_' in display:
    guess = input('Enter a Letter: ')
    guess.lower()
    for i in range(len(chosen_word)):
        if guess in chosen_word:
            letter = chosen_word[i]
            if letter == guess:
                display[i] = letter
        else:
            print("Try again!")
    print(display)
print('You win!')

