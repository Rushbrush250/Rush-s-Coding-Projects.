import pandas as pd
import time

#Getting list contents
df = pd.read_csv('data.csv')


#Function for diffrent lists
def show_(number, dataf):
    if number == 1:
        print(dataf.head())
    if number == 2:
        print(dataf.tail())
    if number == 3:
        print(dataf)
        
while True:
    try:
        user_input = int(input('''Do you want to see the first 5, last 5, or full list? 
  
         - Input "1" for first 5
         - Input "2" for last 5
         - Input "3" for the full list
  
         >> '''))
        if user_input != 1 and user_input != 2 and user_input != 3:
          print("Not a valid answer")
          continue
        show_(user_input, df)
      #Pause for user comprehension
        time.sleep(5)
        loop = input("Another? (y/n) >>")
        if loop.lower() == "y":
            continue
        else:
            break
    except ValueError:
        print("Please put a real number")
print("***")  
