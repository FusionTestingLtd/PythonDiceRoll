import random
import sys


def roll(userData):
    print("\n")
    print("{} {} {} {} {}".format("Using x", userData[0], ",", userData[1], "Sided Dice"))
    i = 1
    total = 0
    while i <= userData[0]:
        tmpval = random.randint(1, userData[1])
        print("{} {} {} {}".format("DiceRoll", i, "=", tmpval))
        total = total + tmpval
        i = i+1
    print("{} {}".format("Total:", total))
    print("\n")


# Get input from the user & set dataType to int
def getUserInput():
    while True:
        try:
            dice = int(input("How many dice to roll?"))
        except ValueError:
            print("Invalid input.. please Enter a number")
            continue
        else:
            break
    while True:
        try:
            sides = int(input("How many sides does the dice have?"))
        except ValueError:
            print("Invalid input.. please Enter a number")
            continue
        else:
            break
    return dice, sides


def menu():
    print("")
    print("1. Roll Dice")
    print("2. Exit")
    while True:
        try:
            choice = int(input("What Would you like to do?"))
        except ValueError:
            print("Invalid Selection! Try again...")
            continue
        else:
            if choice > 2:
                print("Invalid Selection! Try again...")
                continue
            break
    return choice


exitCode = 0
while exitCode != 1:
    if menu() == 2:
        # Exit the program.
        print("...Ending Program")
        exitCode = 1
        exit()
    else:
        # Get the input from the user.
        # Call the Dice Roll function...Dice, Sides Return 'Tuple'
        roll(getUserInput())
