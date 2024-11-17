print("Welcome to QuizQuest!")
print("""
In this game, you can create your own quiz by adding questions and their answers.
- You can save one quiz at a time. Creating a new quiz will overwrite the existing one.
- You can add up to 20 questions for your quiz.
- If you don't want to finish all your questions, you can stop early.
- Once you're done, you can view your quiz by typing 'show' or exit by typing 'quit'.
- You can also start a new quiz by typing 'new' or play the quiz by typing 'play'.

Let's get started!
""")

quiz_data = []

def create_quiz():
    global quiz_data
    quiz_data = []
    getting_question = 0

    while True:
        try:
            question_number = int(input("How many questions do you want to add, between 1 and 20? "))
            print("")
            if question_number < 1 or question_number > 20:
                print("Please enter a number between 1 and 20.")
                print("")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
            print("")

    while getting_question < question_number:
        getting_question += 1
        print(f"Question {getting_question} of {question_number}")
        print("")
        question_add = input("What is the question you want to add? (type 'quit' to stop early) ")
        if question_add.lower() == 'quit':
            print("\nYou chose to stop early. Saving your quiz...\n")
            break
        print("")
        answer_add = input("What is the answer to that question? ")
        print("")
        quiz_data.append({"question": question_add, "answer": answer_add})

    print("Your quiz has been saved!")

def play_quiz():
    score = 0

    if not quiz_data:
        print("You don't have any questions in your quiz.")
        return

    print("\nLet's start the quiz! Answer the following questions:")
    for i, qa in enumerate(quiz_data, start=1):
        print(f"Q{i}: {qa['question']}")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer == qa['answer'].strip().lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {qa['answer']}\n")

    print(f"Your final score is {score} out of {len(quiz_data)}.")
    if score == len(quiz_data):
        print("Perfect score! Well done!")
    elif score > len(quiz_data) / 2:
        print("Good job!")
    else:
        print("Better luck next time!")

create_quiz()

while True:
    command = input("\nType 'show' to view your quiz, 'new' to create a new quiz, 'play' to take the quiz, or 'quit' to exit: ").strip().lower()

    if command == "show":
        if not quiz_data:
            print("You haven't created a quiz yet.")
        else:
            print("\nHere are your questions and answers:")
            for i, qa in enumerate(quiz_data, start=1):
                print(f"Q{i}: {qa['question']}")
                print(f"A{i}: {qa['answer']}")
                print("")
    elif command == "new":
        print("\nCreating a new quiz will overwrite the existing one.")
        confirm = input("Are you sure? Type 'yes' to confirm or 'no' to cancel: ").strip().lower()
        if confirm == "yes":
            create_quiz()
        else:
            print("Cancelled. Your current quiz is unchanged.")
    elif command == "play":
        play_quiz()
    elif command == "quit":
        print("Goodbye! Thanks for playing QuizQuest!")
        break
    else:
        print("Invalid command. Type 'show', 'new', 'play', or 'quit'.")
