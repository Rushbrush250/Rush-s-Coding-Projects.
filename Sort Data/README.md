# Data Sorting Script

This Python script allows you to sort and display data from a CSV file (`output.csv`). The data contains information about fake people, including their names, likes, and dislikes. The user can choose to sort the data by any of these attributes in alphabetical order.

## Features

- **Sort by Name**: Sorts the data alphabetically by the "Names" column.
- **Sort by Like**: Sorts the data alphabetically by the "Likes" column.
- **Sort by Dislike**: Sorts the data alphabetically by the "Dislikes" column.
- **User Input**: The user can choose how they want the data to be displayed. Invalid input prompts the user to try again.

## Usage

1. Ensure that you have the required CSV file (`output.csv`) in the same directory as this script. The CSV file should have the following columns: `Names`, `Likes`, and `Dislikes`.

2. Run the script.

3. The program will prompt you to choose how you'd like to sort the data (by "name", "like", or "dislike").

4. The data will be sorted accordingly, and the result will be printed to the console.

### Example

```bash
$ python sort_data.py
Hello, this data shows fake people with their name, likes and dislikes.
How do you want the data to be shown by, in alphabetical order? (name, like, dislike) >> name
```
The script will then print the sorted DataFrame based on your choice.

## Requirements

- Python 3.x
- pandas library (Install via `pip install pandas`)
