from random import randint
from sys import exit


def main():
    """
    Randomly take a positive number for guessing.
    Prompt for a positive integer as a guess.
    Print result and guess again if not correct yet.
    """
    correct_num = get_num()
    while True:
        guess = make_guess()
        if guess < correct_num:
            print("Too small!")
        elif guess > correct_num:
            print("Too large!")
        else:
            exit("Just right!")


def get_num():
    """
    Randomly generates an integer between 1 and , inclusive.
    """
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                continue
            return randint(1, level)
        except ValueError:
            pass


def make_guess():
    """ "Make a guess"""
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                raise ValueError
            return guess
        except ValueError:
            pass


main()