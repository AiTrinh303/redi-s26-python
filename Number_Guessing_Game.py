# Problem 10: Number Guessing Game
# Keep asking user to guess a number:
# - Too High
# - Too Low
# - Correct! (stop)

import random
target = random.randint(1, 10)
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess > target:
        print("Too High!")
    elif guess < target:
        print("Too Low!")
    else:
        print("Correct! You guessed the number.")
        break