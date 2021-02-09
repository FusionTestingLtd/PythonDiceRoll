import random
import sys


# --------- DICE ROLL FUNCTION -------------
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


# ------------- USER INPUT FUNCTION -------------------
def getUserInput():
    while True:
        try:
            dice = int(input("How many dice to roll?"))
        except ValueError:
            print("Invalid input.. please Enter a number")
            continue
        else:
            if dice > 6 or dice < 1:
                print("Invalid selection! (1-6) Try again...")
                continue
            break
    while True:
        try:
            sides = int(input("How many sides does the dice have?"))
        except ValueError:
            print("Invalid input.. please Enter a number")
            continue
        else:
            if sides > 20 or sides < 4:
                print("Invalid selection! (4-20) Try again..")
                continue
            break
    return dice, sides


# ----------- MENU FUNCTION -----------------
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
            if choice > 2 or choice < 1:
                print("Invalid Selection! Try again...")
                continue
            break
    return choice


# ----------- THE MAIN PROGRAM -----------
exitCode = 0
while exitCode != 1:
    if menu() == 2:
        print("...Ending Program")
        exitCode = 1
        exit()
    else:
        roll(getUserInput())
