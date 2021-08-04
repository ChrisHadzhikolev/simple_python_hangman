import random as rand

word_list = ["aardvark", "baboon", "camel", "wolf", "ginger", "zombie"]

chosen_word = rand.choice(word_list)
print(chosen_word)
guess = input('Enter a Letter: ')
guess.lower()
if guess in chosen_word:
    print("You got it!")
else:
    print("Try again!")
