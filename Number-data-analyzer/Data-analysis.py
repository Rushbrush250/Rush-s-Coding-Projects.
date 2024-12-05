import numpy as np
from scipy import stats as sts
import sys

print('''This is a number analyzer, it can show the mean, median, mode,
sum, and more of all the numbers you give''')
print("")


# Getting amount of numbers
while True:
  try:
    number_of_num = int(input("How many numbers do you want to give? "))
    print("")
    break
  except ValueError:
    print("")
    print("Please enter a number")
    print("")
  
numbers = {}
loop = 0

# Getting numbers

print("Input 's' to stop")
while loop < number_of_num:

    
    loop += 1
    try:
      ans = input(f"What is number {loop} ")
      print("")
      
      # if user enters s, break 
      
      if ans.lower() == "s":
        break 
        #  this is like forces the program to exit 
        raise Exception("User pressed exit ")

      numbers[f"num{loop}"] = int(ans)
    except ValueError:
      print("")
      print(f"erroneus input: {ans}")
      print("")
      

if len(numbers) == 0:
  sys.exit("NO DATA")


# Putting numbers in an np array
number_values = list(numbers.values())
number_array = np.array(number_values)


# Calculating
nmean = np.mean(number_array)
nmedian = np.median(number_array)
nsum = np.sum(number_array)
nmin = np.min(number_array)
nmax = np.max(number_array)
smode = sts.mode(number_array)
if smode.mode == nmin:
  if smode.count > 1:
    smode = smode.mode
  else:
    smode = "<NO MODE>"
else:
  smode = smode.mode


# Output
output_ = f'''------------------------------
          [DATA]

          mean: {nmean}
      
          median: {nmedian}
      
          min: {nmin}
      
          max: {nmax}
      
          mode: {smode}
      
          sum: {nsum}''' 
print(output_)
try:
  saving = int(input('''Do you want to save this data? 
  If yes type the number of the file: (1, 2, 3) >>'''))
  print("")
except ValueError:
  sys.exit("Not a number, no data saved")
  print("")
if 0 > saving or saving > 3:
  sys.exit("Not a valid number, no data saved")
def save_data(saver):
   global output_
   save = open(f"Data-analysis-saving-files//data_saver{saver}.txt", "r+")
   check = save.read()
   if len(check) > 0:
     chocie = input("This file is not empty, do you want to overwrite it (y/n) ?")
     if chocie.lower() == "y":
      save.truncate(0)
      save.seek(0)
      save.write(output_)
      save.close()
      print("")
      print("Data Saved")
     elif chocie.lower() == "n":
      save.close()
   else:
     save.write(output_)
     save.close()
     print("Data Saved")
save_data(saving)
