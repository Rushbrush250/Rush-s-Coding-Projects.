import pandas as pd

# #DataStructure #PandasDataFrame: Creating the movie dataset as a list of dictionaries
movie_data = [
    {"genre": "action", "time_watched_monthly": 3, "interest_level": "high"},
    {"genre": "comedy", "time_watched_monthly": 4, "interest_level": "high"},
    {"genre": "drama", "time_watched_monthly": 2, "interest_level": "medium"},
    {"genre": "horror", "time_watched_monthly": 1, "interest_level": "low"},
    {"genre": "drama", "time_watched_monthly": 3, "interest_level": "high"},
    {"genre": "fantasy", "time_watched_monthly": 2, "interest_level": "medium"},
    {"genre": "comedy", "time_watched_monthly": 1, "interest_level": "low"},
    {"genre": "mystery", "time_watched_monthly": 2, "interest_level": "medium"},
    {"genre": "action", "time_watched_monthly": 3, "interest_level": "high"},
    {"genre": "action", "time_watched_monthly": 1, "interest_level": "low"},
]
movie_df = pd.DataFrame(movie_data)  # #Pandas #DataFrameCreation

def chosen_movie(info_type):
    # #MovieDataAnalysis #UserInput
    if info_type == 1:
        print("Here are the unique genres in the dataset:")
        print(movie_df['genre'].unique())  # #UniqueGenres
        while True:
            choice = input("Do you want some unique info about any of the genres (y/n): ")
            if choice.lower() == "y":
                genre = input("Which genre do you want to know about? ")
                if genre in movie_df['genre'].values:
                    final_data = movie_df[movie_df['genre'] == genre]
                    print(final_data)
                    break
                else:
                    print("Invalid genre, try again")  # #InputValidation
                    continue  # Continue to ask for a valid genre
            elif choice.lower() == "n":
                print("Ok, returning to main menu.")
                break
            else:
                print("Invalid answer, please enter 'y' or 'n'.")  # #InputValidation

    elif info_type == 2:
        # #AverageCalculation #TimeWatchedAnalysis
        print("Here is the average time watched per month:")
        avg_time = movie_df['time_watched_monthly'].mean()
        print(round(avg_time, 2))
        
        choice = input("Do you want to know the average time watched per month based on a genre (y/n)? ")
        all_genres = movie_df['genre'].unique()
        
        while True:
            if choice.lower() == "y":
                print(f"Here are the genres: {', '.join(all_genres)}")
                genre = input("Which genre's average time watched do you want to know? ")
                if genre in all_genres:
                    genre_data = movie_df[movie_df['genre'] == genre]
                    genre_avg_time = genre_data['time_watched_monthly'].mean()
                    print(f"Average time watched per month for '{genre}' genre: {round(genre_avg_time, 2)}")
                    break
                else:
                    print("Invalid genre, try again.")  # #InputValidation
            elif choice.lower() == "n":
                print("Ok, returning to main menu.")
                break
            else:
                print("Invalid input, please enter 'y' or 'n'.")  # #InputValidation

    elif info_type == 3:
        # #InterestLevelAnalysis #DataSummary
        print("Here is the interest level summary:")
        print(movie_df['interest_level'].value_counts())  # #InterestLevelDistribution

# #MainFunction
print("Hello, you can get specifics about any of the data sets!")

dataset = input("Which dataset do you want to look at? (movie only): ").lower()

if dataset == "movie":
    try:
        info = int(input('''What do you want to know about the movie dataset?
                         (Input 1 for genre, Input 2 for time watched monthly, Input 3 for interest level summary): '''))
        if info in [1, 2, 3]:
            chosen_movie(info)  # #FunctionCall #ChosenMovie
        else:
            print("Invalid input, please choose 1, 2, or 3.")  # #InputValidation
    except ValueError:
        print("Invalid input, please enter a number.")  # #ErrorHandling
else:
    print("Movie only, sorry")
