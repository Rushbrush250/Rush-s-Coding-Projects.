# Versatile Number Manipulation Application

This is a simple Python application designed to provide basic number manipulation functions. It allows the user to:

1. **Sort and remove duplicates from a list of numbers.**
2. **Count the frequency of each number in a list.**
3. **Perform basic arithmetic operations on two numbers.**

## Features

- **Option 1**: Sorts the entered numbers and removes any duplicates.
- **Option 2**: Counts how many times each number appears in the list.
- **Option 3**: Performs arithmetic operations (addition, subtraction, multiplication, division) on two input numbers.

## Usage

1. **Sorting and Removing Duplicates**
    - The user is prompted to input a list of numbers.
    - After entering the specified number of values, the list is sorted and any duplicate entries are removed.

2. **Counting Occurrences of Numbers**
    - The user is asked to input a list of numbers.
    - The application counts and displays the frequency of each number in the list.

3. **Basic Arithmetic Operations**
    - The user inputs two numbers and chooses an operator (add, subtract, multiply, or divide).
    - The result of the operation is then calculated and displayed.

## Code Breakdown

1. **Sorting and Removing Duplicates**
    - Users provide a list of numbers.
    - The list is sorted and duplicates are removed using the `set()` function.

2. **Counting Occurrences**
    - A list of numbers is entered by the user.
    - A dictionary is used to track the count of each number, which is then displayed in a pandas DataFrame.

3. **Arithmetic Operations**
    - The user can input two numbers and select an operation.
    - A simple function is used to perform the requested operation.


### Input Validation

- The program includes input validation to ensure that only valid numbers are entered.
- In case of invalid input, the user is prompted again.

### Requirements

- **pandas** library is required for displaying the count of numbers in a DataFrame.
- Ensure you have the necessary libraries installed by running:
    ```bash
    pip install pandas
    ```

## Conclusion

This application provides a simple and user-friendly interface for manipulating numbers, including sorting, counting occurrences, and performing basic arithmetic operations.

