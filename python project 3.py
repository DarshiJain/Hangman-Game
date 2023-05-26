#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     02-05-2023
# Copyright:   (c) HP 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import hangman_stages
import words_file
#word_list = ["apple","beautiful","potato"]
lives = 6
chosen_word = random.choice(words_file.words)
print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display += "_"
print(display)
game_over = False
while not game_over:
    guessed_letter = input("GUESS A LETTER :").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("YOU LOSE!!")

    if "_" not in display:
        game_over = True
        print("YOU WIN!!")
    print(hangman_stages.stages[lives])




