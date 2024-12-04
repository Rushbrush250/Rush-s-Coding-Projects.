import numpy as np
import random as rd
import time as t

loop = 0
stored = np.array([
    [[1, 2], [3, 4], [5, 6], [7, 8]],  # row 0
    [[9, 10], [11, 12], [13, 14], [15, 16]],  # row 1
    [[17, 18], [19, 20], [21, 22], [23, 24]]  # row 2
])

def random_choose(iterations, number, data):
    if iterations == 1:
        data[0, 0, 0] = number
    if iterations == 2:
        data[0, 0, 1] = number
    if iterations == 3:
        data[0, 1, 0] = number
    if iterations == 4:
        data[0, 1, 1] = number
    if iterations == 5:
        data[0, 2, 0] = number
    if iterations == 6:
        data[0, 2, 1] = number
    if iterations == 7:
        data[0, 3, 0] = number
    if iterations == 8:
        data[0, 3, 1] = number
    if iterations == 9:
        data[1, 0, 0] = number
    if iterations == 10:
        data[1, 0, 1] = number
    if iterations == 11:
        data[1, 1, 0] = number
    if iterations == 12:
        data[1, 1, 1] = number
    if iterations == 13:
        data[1, 2, 0] = number
    if iterations == 14:
        data[1, 2, 1] = number
    if iterations == 15:
        data[1, 3, 0] = number
    if iterations == 16:
        data[1, 3, 1] = number
    if iterations == 17:
        data[2, 0, 0] = number
    if iterations == 18:
        data[2, 0, 1] = number
    if iterations == 19:
        data[2, 1, 0] = number
    if iterations == 20:
        data[2, 1, 1] = number
    if iterations == 21:
        data[2, 2, 0] = number
    if iterations == 22:
        data[2, 2, 1] = number
    if iterations == 23:
        data[2, 3, 0] = number
    if iterations == 24:
        data[2, 3, 1] = number

# Giving the array random numbers
while loop < 24:
    random_number = rd.randint(1, 30)
    random_choose(loop + 1, random_number, stored)  # Corrected index by adding 1 to loop
    loop += 1

# Now, choosing a random **pair** (2 numbers) from the array
flattened_pairs = stored.reshape(12, 2)  # Flatten to 1D and get pairs (2 numbers)
random_pair = rd.choice(flattened_pairs)  # Randomly choose a pair from the flattened array
random_pair2 = rd.choice(flattened_pairs)

print('''Game Instructions:

1. Your Goal: Find two groups of numbers that add up to a target pair.

2. Example:
   - Groups:
     Group 1: (6, 8)
     Group 2: (9, 0)
     Group 3: (7, 4)
   - Target: (13, 12)

3. How to Play:
   - Pick the first group. For example, press 1 for Group 1.
   - Pick the second group. For example, press 3 for Group 3.

4. Winning:
   - If the numbers add up to the target (e.g., 6+7=13 and 8+4=12), you win.
   - You can add the same group 2 times.
   - If not, try again.
   - Your end time will be displayed whether you win or lose

''')

# Combined pair target (sum of selected pairs)
target_pair = random_pair + random_pair2
print(f'''********************************************************************
                         All Pairs

            1.{flattened_pairs[0]}          2.{flattened_pairs[1]}

            3.{flattened_pairs[2]}           4.{flattened_pairs[3]}

            5.{flattened_pairs[4]}           6.{flattened_pairs[5]}

            7.{flattened_pairs[6]}           8.{flattened_pairs[7]}

            9.{flattened_pairs[8]}           10.{flattened_pairs[9]}

            11.{flattened_pairs[10]}           12.{flattened_pairs[11]}

                   --Combined Pair--
                      {target_pair}         What is the two pairs that makes the combined pair?

''')

# Input validation for the first pair
timer_start = t.perf_counter()
while True:
    try:
        user_ans1 = int(input("First pair? (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12): "))
        print("")
        if 1 <= user_ans1 <= 12:
            break
        else:
            print("Please give a number between 1 and 12.")
            print("")
    except ValueError:
        print("Please give a valid number.")
        print("")

# Input validation for the second pair
while True:
    try:
        user_ans2 = int(input("Second pair?: "))
        print("")
        if 1 <= user_ans2 <= 12:
            break
        else:
            print("Please give a number between 1 and 12.")
            print("")
    except ValueError:
        print("Please give a valid number.")
        print("")

# Getting the actual pairs based on user selection
pair1 = flattened_pairs[user_ans1 - 1]  # Convert 1-based index to 0-based
pair2 = flattened_pairs[user_ans2 - 1]  # Convert 1-based index to 0-based
timer_end = t.perf_counter()
timer_passed = np.subtract(timer_end,timer_start)
# Check if the sum of selected pairs matches the target
if (pair1[0] + pair2[0] == target_pair[0]) and (pair1[1] + pair2[1] == target_pair[1]):
    print("You win! The pairs add up correctly.")
    print("")
    print(f"Your time: {timer_passed:.2}")
else:
    print("Try again! The pairs don't add up to the target.")
    print("")
    print(f"Your time: {timer_passed:.2} seconds")
