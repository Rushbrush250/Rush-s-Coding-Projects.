# Movie Dataset Interactive Exploration

This project provides an interactive way to explore a movie dataset. The dataset contains information about different movie genres, the time spent watching them each month, and the viewer's interest level in each genre. This script allows you to interact with the dataset and obtain detailed insights based on user input.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [How to Run](#how-to-run)
- [Dataset Description](#dataset-description)
- [Functions](#functions)
- [Example Usage](#example-usage)
- [Error Handling](#error-handling)
- [License](#license)

## Project Overview

The main purpose of this project is to provide users with an interactive way to analyze a movie dataset. Users can learn about the various genres, get average time spent watching movies per month, and summarize the distribution of interest levels in the dataset.

The dataset is structured as a list of dictionaries with the following information:

- `genre`: The genre of the movie (e.g., Action, Comedy, Drama, etc.)
- `time_watched_monthly`: The average time in hours spent watching movies in that genre per month.
- `interest_level`: The user's interest in the genre (e.g., "low", "medium", "high").

## Features

- **Explore Unique Genres**: Get a list of all unique genres in the dataset and view specific information about them.
- **Average Time Watched**: View the average time spent watching movies in all genres or for a specific genre.
- **Interest Level Summary**: Get a summary of the distribution of interest levels across all genres.
- **Interactive Interface**: The user is prompted to make choices and provide inputs to explore the data further.

## How to Run

To run this script, ensure you have **Python** installed on your machine, along with the `pandas` library.

### Step 1: Install pandas (if you don't have it already)

If you don't have `pandas` installed, you can install it via pip:

```bash
pip install pandas
```

### Step 2: Run the script
You can run the script directly in your terminal or command prompt:

```bash
python movie_explorer.py
```
