import random

def get_unique_random(UN):
    while True:
        Rand = random.randint(1, 20)
        if Rand in UN:
            continue
        UN.add(Rand)
        return Rand

# Store unique random numbers for the computer
UN = set()
AR = get_unique_random(UN)
BR = get_unique_random(UN)
CR = get_unique_random(UN)

print("Let's play a guessing game! Choose 3 numbers between 1 and 20 for me to guess.")
N1 = int(input("What is your first number? "))
N2 = int(input("What is your second number? "))
N3 = int(input("And your third and last number? "))

PG = set()  # Computer's guesses
YG = set()  # Player's guesses
CA = 0  # Count of computer's correct guesses
PA = 0  # Count of player's correct guesses

def comp_g():
    global CA
    CG = random.randint(1, 20)
    while CG in PG:
        CG = random.randint(1, 20)  # Keep generating if already guessed
    PG.add(CG)
    print(f"Computer guesses: {CG}")
    if CG in (N1, N2, N3):
        print(f"Computer guessed one of your numbers: {CG}")
        CA += 1
    else:
        print("Computer's guess was wrong.")

def play_g():
    global PA
    YT = int(input("What's your guess? "))
    if YT in YG:
        print("You already guessed that number.")
    elif YT in (AR, BR, CR):
        YG.add(YT)
        print(f"You guessed one of my numbers: {YT}")
        PA += 1
    else:
        print("Wrong guess, try again.")

# Game loop for back-and-forth guessing
while True:
    comp_g()  # Computer's turn to guess

    if CA == 3:
        print("The computer has guessed all of your numbers. You lose!")
        break

    play_g()  # Player's turn to guess

    if PA == 3:
        print("Congratulations! You've guessed all of my numbers!")
        break
