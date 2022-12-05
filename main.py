import os
from art import logo
from random import *


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    random_number = randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
    if difficulty == "easy":
        guesses = 10
    else:
        guesses = 5
    print(guesses)

    while guesses > 0:
        print(f"You have {guesses} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        if player_guess == random_number:
            print(f"THAT'S IT! Number in my mind is {random_number}.")
            break
        elif player_guess > random_number:
            print("Too high!")
            guesses -= 1
        else:
            print("Too low!")
            guesses -= 1

    if guesses == 0:
        print("You lose!")

    while input("Do you want to play again? Type 'y' or 'n': ").lower() == "y":
        os.system('cls')
        play_game()


play_game()
