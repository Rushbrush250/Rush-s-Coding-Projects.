SUPERMARK = ["apple", "banana", "orange", "berries",
             "broccoli", "carrot", "celery", "peas",
             "blt", "philly cheesesteak", "egg salad sandwich", "pbj"]



VEGGIES = [
    'Broccoli',
    'Carrot',
    'Celery',
    'Peas'
          ]
FRUITS = [
    'Apple',
    'Banana',
    'Berries',
    'Orange'
]

SANDWICHES = [
    'BLT',
    'Philly cheesesteak',
    'Egg salad sandwich',
    'PBJ'
]


# Adding functions will help us modularize our code
# and make it easier to write logic

def welcome_message():
    """
    Prints Welcome Message
    """

    print('''Welcome to the supermarket!
      If you want to know what you can get type "ask"
    if you want to know what you can get.
    Make sure to put the exact name of the item listed in the section.
    Same for when typing the section. Enjoy!

          ''')

def show_deli_sections():
    """
    Shows the different sections of the supermarket
    """
    print('''The deli sections are:
        Sandwich
        Meal

        ''')
def show_produce():
    print('''The produce sections are:
        Fruit
        Veggies

        Type a section to know what you can get.

        ''')
def show_veggies():
    print('The veggies are:\n')
    for veg in VEGGIES:
        print(veg)
    print("Type a vegetable to buy it")

def show_fruits():

    print('The fruits are:\n')
    for veg in VEGGIES:
        print(veg)
    print("\nType a fruit to buy it\n")

def show_sandwich():
    print('The sandwiches are:\n')
    for san in SANDWICHES:
        print(san)
    print("\n Type a Sandwich to buy it...\n")
# call welcome message function
welcome_message()
card = 100
while True:
  A = input(">")
  if A.lower() in SUPERMARK:
    if A.lower() == "apple":
      card -= 3
    elif A.lower() == "banana":
      card -= 1
    elif A.lower() == "orange":
      card -= 2
    elif A.lower() == "berries":
      card -= 4
    elif A.lower() == "broccoli":
      card -= 2
    elif A.lower() == "carrot":
      card -= 1
    elif A.lower() == "celery":
      card -= 2
    elif A.lower() == "peas":
      card -= 3
    elif A.lower() == "blt":
      card -= 6
    elif A.lower() == "philly cheesesteak":
      card -= 9
    elif A.lower() == "egg salad sandwich":
      card -= 5
    elif A.lower() == "pbj":
      card -= 5
    print(f'''
    You bought {A}. Your balance on your card is now {card}
          ''')
    continue
  elif A.lower() == "ask":
    print('''The sections are:
    Produce
    Deli

    Type a section to know what you can get.

    ''')
    continue
  elif A.lower() == "produce":
    show_produce()
    continue
  elif A.lower() == "deli":
    show_deli_sections()
    continue
  elif A.lower() == "fruit":
    show_fruits()
    continue
  elif A.lower() == "veggies":
    show_veggies()
    continue
  elif A.lower() == "sandwich":
    show_sandwich()
    continue

