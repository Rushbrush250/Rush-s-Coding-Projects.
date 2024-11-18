# game.py

import invest
import random as rd

company_names = [
    "TechnoSpark Innovations",
    "PixelPioneer Solutions",
    "QuantumLeap Enterprises",
    "FusionCore Systems",
    "NexaLabs Technologies",
    # Add more companies here...
]

cash = 100000
days = 0
name = input("You are an investor trying to gain wealth and your name is? ")
print("")
print(f"That's your name, {name}. You have 10 days to get rich.")
print("")

while days < 10:
    compy1, compy2, compy3, compy4 = invest.unique_compname(company_names)
    days += 1
    choose = input(f'''Day {days} -------------------------------------------------------------------       
                               You look at the current companies before you. 
       
         1. {compy1}       
         2. {compy2}        
         3. {compy3}         
         4. {compy4}
         
                        Your cash is {cash}
                        Which one do you choose? (Enter the number exactly) >>''')
    print("")

    if choose == '1' or choose == '2' or choose == '3' or choose == '4':
        company = compy1 if choose == '1' else (compy2 if choose == '2' else (compy3 if choose == '3' else compy4))

        while True:
            try:
                invested = int(input("How much are you investing? "))
                print("")
                
                if invested > cash:
                    print("That is not in your budget, try again.")
                    print("")
                elif invested < 0:
                    print("That's not possible, try again.")
                    print("")
                else:
                    modified_investment = invest.luck(invested)
                    cash -= invested
                    cash += modified_investment
                    print(f"Your current cash balance is: {cash}")
                    break
            except ValueError:
                print("That is not a number, try again.")
                print("")
    else:
        print("That is not a company, You don't invest today.")
else:
    print("")
    print(f"Your ending balance was {cash}")
    print("")
    
    if cash > 150000:
        print(f"Excellent job, {name}! You've made a tremendous profit of {cash - 100000}! Your final balance is {cash}. You're a master investor now, with a sharp eye for profitable opportunities. You turned your initial investment into something extraordinary. Keep going, and you could become a mogul!")
    elif 110000 <= cash <= 150000 or 90000 <= cash < 100000:
        print(f"Nice work, {name}. You've managed to grow your wealth a bit, with a final balance of {cash}. While it's not a huge win, a small gain is still progress! On the flip side, if you're on the losing end, you're just one step away from bouncing back. A small loss is just a part of the game—use the lessons learned to make better decisions next time.")
    elif cash < 90000:
        print(f"Well, {name}, it's been a tough ride. Your final balance is {cash}, which means you've taken quite a loss. But don’t be discouraged—every investor faces setbacks. The most successful ones learn from these challenges and come back even stronger. Use this as a stepping stone to refine your strategy and make smarter choices next time. The future is still bright!")
