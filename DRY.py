# Dont't repeat your self
import random
winning_number = random.randint(1,100)
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
        else:
                print("Too high")
        guess += 1
        number = int(input("Guess again: "))