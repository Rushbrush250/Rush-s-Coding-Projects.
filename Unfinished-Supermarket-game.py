supermark = ["apple", "banana", "orange", "berries",
             "broccoli", "carrot", "celery", "peas",
             "blt", "philly cheesesteak", "egg salad sandwich", "pbj"]
print('''Welcome to the supermarket!
  If you want to know what you can get type "ask"
if you want to know what you can get.
Make sure to put the exact name of the item listed in the section.
Same for when typing the section. Enjoy!

''')
card = 100
while True:
  A = input("")
  if A.lower() in supermark:
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
    print('''The produce sections are:
    Fruit
    Veggies

    Type a section to know what you can get.

    ''')
    continue
  elif A.lower() == "deli":
    print('''The deli sections are:
    Sandwich
    Meal

    ''')
    continue
  elif A.lower() == "fruit":
    print('''The fruits are:
    Apple
    Banana
    Berries
    Orange

    Type a fruit to buy it.

    ''')
    continue
  elif A.lower() == "veggies":
    print('''The veggies are:
    Broccoli
    Carrot
    Celery
    Peas

    Type a vegtable to buy it

    ''')
    continue
  elif A.lower() == "sandwich":
    print('''The sandwiches are:
    BLT
    Philly cheesesteak
    Egg salad sandwich
    PBJ

    ''')
    continue

