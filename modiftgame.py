# MODIFT NUMBER GAME GUESS

import random
winning_number = 43
guess = 1
number = int(input("Guess any number between 1 and 100: "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"you win, and you guessed this in {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print("too low")
            guess += 1
            number = int(input("Guess again: "))
        else:
            print("Too high")
            guess += 1
            number = int(input("Guess again: "))

