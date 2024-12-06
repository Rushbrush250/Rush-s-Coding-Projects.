import numpy as np
import random as rd
import time
import os


h = 0
while True:
  if h > 10:
    break
  numbers_used = rd.randint(0, 100)
  chocie_of_array1 = rd.choice([1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60])
  chocie_of_array2 = int(np.divide(60, chocie_of_array1))
  changing_array = np.zeros((60, 1))
  changing_array.fill(numbers_used)
  changing_array.shape = (chocie_of_array1, chocie_of_array2)
  print(changing_array)
  time.sleep(3)
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
  h += 2
