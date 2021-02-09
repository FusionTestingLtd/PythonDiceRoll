import random


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
    # NUMBER OF DICE INPUT
    is_valid = 0
    while is_valid != 1:
        dice = input("How many dice?")
        try:
            int(dice)
        except ValueError:
            try:
                float(dice)
            except ValueError:
                print("Sorry you entered a string, Please enter a whole number\n")
                continue
            else:
                print("Sorry you entered a decimal number, Please enter a whole number\n")
            continue
        else:
            dice = int(dice)
            if dice > 6 or dice < 1:
                print("Out of range, try between 1 and 6\n")
                continue
            is_valid = 1

    # NUMBER OF SIDES INPUT
    is_valid = 0
    while is_valid != 1:
        sides = input("How many sides does the dice have?")
        try:
            int(sides)
        except ValueError:
            try:
                float(sides)
            except ValueError:
                print("Sorry you entered a string, Please enter a whole number \n")
                continue
            else:
                print("Sorry you entered a decimal number, Please enter a whole number\n")
            continue
        else:
            sides = int(sides)
            if sides > 20 or sides < 4:
                print("Out of range, try between 4 and 20\n")
                continue
            is_valid = 1
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
            print("you didn't enter a number :-)")
            continue
        else:
            if choice > 2 or choice < 1:
                print("Out of range, try 1 or 2 instead :-)")
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
