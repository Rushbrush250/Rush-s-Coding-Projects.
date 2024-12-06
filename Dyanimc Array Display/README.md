# Random Number Array Generator

This Python script generates a random 2D array with a size determined by random factors, and then displays the array in the terminal. The program utilizes NumPy for array manipulation and random number generation to produce a unique array every cycle. The array is cleared after a 3-second delay for dynamic updates.

## Features
- Generates a random number between 0 and 100 for use in array initialization.
- Randomly selects a divisor for creating a 2D array of size 60x1.
- Divides 60 by a randomly chosen integer to determine the array's shape.
- Prints the array to the terminal, waits for 3 seconds, and clears the terminal screen for the next iteration.
- Stops execution after generating 6 unique arrays (when the counter `h` exceeds 10).

## Requirements
- Python 3.x
- NumPy library (install using `pip install numpy`)

## How to Run

1. Clone this repository or download the script to your local machine.
2. Ensure you have Python 3.x installed.
3. Install the required dependencies by running:
   ```bash
   pip install numpy
