import random
import operator

def ask_question(quest1, opp1, quest2, opp2, quest3, opp3, quest4, opp4, quest5):
    # Start with the first two questions and their operation
    if opp1 == operator.add:
        result = quest1 + quest2
    elif opp1 == operator.sub:
        result = quest1 - quest2
    elif opp1 == operator.mul:
        result = quest1 * quest2

    # Apply the second operation
    if opp2 == operator.add:
        result += quest3
    elif opp2 == operator.sub:
        result -= quest3
    elif opp2 == operator.mul:
        result *= quest3

    # Apply the third operation
    if opp3 == operator.add:
        result += quest4
    elif opp3 == operator.sub:
        result -= quest4
    elif opp3 == operator.mul:
        result *= quest4

    # Finally, add the last question
    result += quest5

    return result

def generate_question():
    # Generate random numbers and operations
    Quest1, Quest2, Quest3, Quest4, Quest5 = [random.randint(1, 20) for _ in range(5)]
    Opp1, Opp2, Opp3, Opp4 = [random.choice([operator.add, operator.sub, operator.mul]) for _ in range(4)]

    return Quest1, Opp1, Quest2, Opp2, Quest3, Opp3, Quest4, Opp4, Quest5

player1_score = 0
player2_score = 0

while player1_score < 5 and player2_score < 5:
    # Generate a new question for each player
    Quest1, Opp1, Quest2, Opp2, Quest3, Opp3, Quest4, Opp4, Quest5 = generate_question()

    # Ask Player 1
    print("Player 1's turn")
    print(f"What is {Quest1} {Opp1.__name__} {Quest2} {Opp2.__name__} {Quest3} {Opp3.__name__} {Quest4} + {Quest5}?")

    while True:
        try:
            player1_answer = int(input("Your answer: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    correct_answer = ask_question(Quest1, Opp1, Quest2, Opp2, Quest3, Opp3, Quest4, Opp4, Quest5)

    if player1_answer == correct_answer:
        print("Correct! Player 1 scores a point.")
        player1_score += 1
    else:
        print(f"Wrong! The correct answer was {correct_answer}.")

    # Generate a new question for Player 2
    Quest1, Opp1, Quest2, Opp2, Quest3, Opp3, Quest4, Opp4, Quest5 = generate_question()

    # Ask Player 2
    print("\nPlayer 2's turn")
    print(f"What is {Quest1} {Opp1.__name__} {Quest2} {Opp2.__name__} {Quest3} {Opp3.__name__} {Quest4} + {Quest5}?")

    while True:
        try:
            player2_answer = int(input("Your answer: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    correct_answer = ask_question(Quest1, Opp1, Quest2, Opp2, Quest3, Opp3, Quest4, Opp4, Quest5)

    if player2_answer == correct_answer:
        print("Correct! Player 2 scores a point.")
        player2_score += 1
    else:
        print(f"Wrong! The correct answer was {correct_answer}.")

    print(f"\nScores: Player 1: {player1_score}, Player 2: {player2_score}\n")

# Determine the winner
if player1_score == 5:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
