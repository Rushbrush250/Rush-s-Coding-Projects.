import pandas as pd
import random as rd

numbers = {}
def bot():
      random_number1 = rd.randint(1, 100)
      random_number2 = rd.randint(1, 100)
      random_number3 = rd.randint(1, 100)
      random_number4 = rd.randint(1, 100)
      random_number5 = rd.randint(1, 100)
      return random_number1, random_number2, random_number3, random_number4, random_number5

print('''You will create a number dataset with an bot 
      and you can only choose numbers between 1 and 100, you go first.''')
print("")

loop = 1
while True: 
    try:
        numbers[f"Num{loop}"] = int(input(f"Enter number {loop}/5>>"))
        if not 1 <= numbers[f"Num{loop}"] <= 100:
            print("Hey, you can only choose numbers between 1 and 100")
            print("")
            loop -= 1
        loop += 1
        if loop == 6:
            break
    except ValueError:
        print("That's not a number try again")
        print("")

bot_numbers1, bot_numbers2, bot_numbers3, bot_numbers4, bot_numbers5 = bot()
number_ = 0
print(f'''

The bots numbers are:
{bot_numbers1}
{bot_numbers2}
{bot_numbers3}
{bot_numbers4}
{bot_numbers5}

''')

dataset = {
    "Player's Numbers": [numbers["Num1"], numbers["Num2"], numbers["Num3"], numbers["Num4"], numbers["Num5"]],
    "Bot's Numbers": [bot_numbers1, bot_numbers2, bot_numbers3, bot_numbers4, bot_numbers5]
}
df = pd.DataFrame(dataset)

while True:
    option1 = input("Do you want to name the dataset's columns? (y/n) >>")
    if option1.lower() == "y":
        column1 = input("Enter the name of your dataset's column >>")
        column2 = input("Enter the name of the bot dataset'$ column >>")
        df.columns = [column1, column2]
        print("")
    elif option1.lower() == "n":
        print("")
    else:
        print("Invalid option, you can only choose 'y' for yes and 'n' for no")
        print("")
    option2 = input("Do you want the dataset's columns to be uppercase? (y/n) >>")
    if option2.lower() == "y":
        df.columns = df.columns.str.upper()
        print("")
    elif option2.lower() == "n":
        print("")
    else:
        print("Invalid option, you can only choose 'y' for yes and 'n' for no")
        print("")
    break

df.index = df.index + 1
print(df)
