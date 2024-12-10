# CSV Viewer Python Script

This Python script allows you to interactively view a CSV file (`data.csv`) with a simple menu system. The script uses the `pandas` library to load the CSV file and provides users with three options for displaying data:

1. The first 5 rows of the CSV file.
2. The last 5 rows of the CSV file.
3. The full content of the CSV file.

## Requirements

- Python 3.x
- `pandas` library (You can install it with `pip install pandas`)

## File Structure

- `data.csv`: A CSV file containing data with columns `Name`, `Age`, and `City`.

### Example Content of `data.csv`:
Name,Age,City John,25,New York Alice,30,Boston Bob,22,Moscow Bill,45,London Kate,57,Berlin Tad,37,Tokyo Gabe,18,Paris Sophia,28,Stockholm Xavier,32,Madrid Caden,29,Rome

## Script Overview

### Code Walkthrough

1. **Imports**: 
   - `pandas` is used to handle CSV data.
   - `time` is used for pausing the script to allow user comprehension between inputs.

2. **Loading the CSV File**: 
   - The CSV file (`data.csv`) is read into a pandas DataFrame named `df` using `pd.read_csv('data.csv')`.

3. **Function `show_`**: 
   - This function takes two parameters: `number` (to specify which part of the DataFrame to show) and `dataf` (the DataFrame itself).
   - Depending on the user's input (`1`, `2`, or `3`), it prints:
     - First 5 rows (if `1`).
     - Last 5 rows (if `2`).
     - Entire DataFrame (if `3`).

4. **User Interaction**:
   - A `while True` loop is used to continuously prompt the user for input.
   - The user is asked to choose between showing the first 5 rows, the last 5 rows, or the full list.
   - After displaying the requested data, the script pauses for 5 seconds using `time.sleep(5)` to allow the user to comprehend the output.
   - The user is then asked if they want to perform another operation. If they input "y", the loop continues. If "n", the loop breaks and the script ends.

5. **Error Handling**:
   - If the user inputs anything other than "1", "2", or "3", the script will print "Not a valid answer" and prompt the user again.
   - If a non-numeric input is provided, the script catches the `ValueError` and asks the user to provide a valid number.

## Running the Script

1. Ensure you have the necessary Python environment and libraries:
   ```bash
   pip install pandas
2. Place the script and data.csv file in the same directory.
3. Run the Python script:
   `python csv_viewer.py`
4. Follow the interactive prompts to view the data in the CSV file.
