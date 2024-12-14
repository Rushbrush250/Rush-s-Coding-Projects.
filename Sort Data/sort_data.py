import pandas as pd

# Read the CSV file
info_df = pd.read_csv('output.csv')

def choose(user_choice):
    # Using the global variable `info_df`
    global info_df
    while True:
        if user_choice.lower() == "name" or user_choice.lower() == "names":
            info_df.set_index("Names", inplace=True)
            info_df = info_df.sort_values(by="Names")
            break
        elif user_choice.lower() == "like" or user_choice.lower() == "likes":
            info_df.set_index("Likes", inplace=True)
            info_df = info_df.sort_values(by="Likes")
            break
        elif user_choice.lower() == "dislike" or user_choice.lower() == "dislikes":
            info_df.set_index("Dislikes", inplace=True)
            info_df = info_df.sort_values(by="Dislikes")
            break
        else:
            user_choice = input('''Invalid input, try again, 
            How do you want the data to be shown by, in alphabetical order? (name, like, dislike) >>''')

print("Hello, this data shows fake people with their name, likes and dislikes.")
choice = input("How do you want the data to be shown by, in alphabetical order? (name, like, dislike) >>")
choose(choice)
print(info_df)
