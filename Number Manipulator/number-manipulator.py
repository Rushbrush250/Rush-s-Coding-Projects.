import pandas as pd
import sys


print('''This is A versatile application for manipulating numbers.
- input 1 for sorting and removing any duplicates of numbers
- input 2 for counting the number of times each number shows up
- input 3 for performing a basic number operation on two numbers
''')
user_choice = input(">>")
    
if user_choice == "1":
    li = []
    looping_number = 1
    adding_number = ""
    try:
      amount_of_numbers =  int(input("How many numbers do you want to put"))
    except ValueError:
        print("That's not a vaild number")
        sys.exit()
    while True:
        try:
            adding_number = int(input(f"Add number {looping_number} or stop adding by inputting 's'>>"))
            li.append(adding_number)
            looping_number += 1
            if looping_number == amount_of_numbers + 1:
                break
        except ValueError:
                print("Invalid input")
                print("")
    li.sort()
    li = list(set(li))
    print(f"The new list sorted and without duplicates: {li}")

elif user_choice == "2":
    looping_number = 1
    looping_dictionary = 1
    li = []
    di = {}
    try:
        amount_of_numbers = int(input("How many numbers do you want to put"))
    except ValueError:
        print("That's not a valid number")
        sys.exit()
    
    while looping_number <= amount_of_numbers:
        try:
            adding_number = int(input(f"Add number {looping_number}: "))
            li.append(adding_number)
            looping_number += 1
        except ValueError:
            print("Invalid input")
            print("")
    li.sort()
    tracking_number = 0
    for item in li:
        if tracking_number != item:
            di[f"num{item}"] = li.count(item)
            tracking_number = item
    df = pd.DataFrame(di, index=["Number Count"])
    print(df)

elif user_choice == "3":
  def op(num1, num2, operator):
        if operator == "add":
            return num1 + num2
        if operator == "subtract":
            return num1 - num2
        if operator == "multiply":
            return num1 * num2
        if operator == "divide":
            return num1 / num2
        else:
            return "Invalid operator"
  while True:
    try:
        number1 = float(input("Enter the first number: >>"))
        operator = input('''Here are the list of operators you can choose:
        - add
        - subtract
        - multiply
        - divide
        
        input the operator you want to use: >>''')
        number2 = float(input("Enter the second number: >>"))
        break
    except ValueError:
        print("Invalid input")
        print("")
  final_output = op(number1, number2, operator)
  print("")
  if final_output == "Invalid operator":
    print(final_output)
    sys.exit()
  if final_output == int(final_output):
    final_output = int(final_output)
  print(f"The answer is: {final_output}")
