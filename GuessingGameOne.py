#guessing game
#Generate a random number between 1 and 9
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random

randNum = random.randint(1,9)
guess = 0
count = 0

while guess != randNum and guess != "exit":
    guess = input("Guess a number 1-9: ")

    if guess == exit:
        break

    guess = int(guess)
    count += 1

    if guess > randNum:
        print("too high")

    elif guess < randNum:
        print("too low")

    else:
        print("right!")
        print("It only took you", count, "times!")

input()


