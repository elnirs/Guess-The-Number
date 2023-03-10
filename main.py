# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

print(art.logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

## Randomizing a number from 1 to 100
chosen_number = random.randint(1, 100)
print(f"Psst. The random number is {chosen_number}.")

# Choosing the difficulty level
attempts = -1

while attempts == -1:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Wrong difficulty input")
        attempts = -1

# game on
guess = -1

while attempts > 0 and guess != chosen_number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}.")
    elif guess < chosen_number:
        print("Too low.")
        attempts -= 1
    elif guess > chosen_number:
        print("Too high.")
        attempts -= 1

    if attempts > 0 and guess != chosen_number:
        print("Guess again.")
    if attempts == 0:
        print("You've run out of guesses, you lose.")


