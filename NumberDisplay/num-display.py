import numpy as np

numbers = np.load("NumberDisplay//numbers.npy")
# Print the current array in a readable format
print(f'''

        1.({int(numbers[0,0])}) | 2.({int(numbers[0,1])}) | 3.({int(numbers[0,2])}) | 4.({int(numbers[0,3])})

        5.({int(numbers[1,0])}) | 6.({int(numbers[1,1])}) | 7.({int(numbers[1,2])}) | 8.({int(numbers[1,3])})

        9.({int(numbers[2,0])}) | 10.({int(numbers[2,1])}) | 11.({int(numbers[2,2])}) | 12.({int(numbers[2,3])})

        13.({int(numbers[3,0])}) | 14.({int(numbers[3,1])}) | 15.({int(numbers[3,2])}) | 16.({int(numbers[3,3])})

        ''')

change = input("Do you want to change a number? (y/n): >>")

if change.lower() == "y":
    while True:
        try:
            # Prompt for the number to change (1-16)
            input_number = int(input("What number do you want to change? 1-16: >>"))
            if input_number > 16 or input_number < 1:
                print("Please enter a number between 1 to 16")
                continue

            # Find the corresponding row and column based on the input number
            row = (input_number - 1) // 4
            col = (input_number - 1) % 4

            # Prompt for the new value
            changing = int(input("What number do you want to change it to?: >>"))

            # Update the number in the original array
            numbers[row, col] = changing

            # Save the updated array back to the file
            np.save("numbers.npy", numbers)
            print("Saved")
            break
        except ValueError:
            print("Please enter a valid number")
            continue
elif change.lower() == "n":
    print("Ok")
else:
    print("Invalid input")
