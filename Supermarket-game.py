supermark = ["apple", "banana", "orange", "berries",
             "broccoli", "carrot", "celery", "peas",
             "blt", "philly cheesesteak", "egg salad sandwich", "pbj",
             "egg roll", "fried chicken", "soup", "pizza",
             "milk", "cheese", "butter", "yogurt", "egg",
             "beef", "pork", "lamb",
             "chicken", "turkey", "duck",
             "salmon", "shrimp", "tuna"]
print('''Welcome to the supermarket!
  If you want to know what you can get type "ask", also type "quit" to leave.
Make sure to put the exact name of the item listed in the section.
Same for when typing the section. Enjoy!

''')
receipt = []
card = 100
while card > 0 :
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
    elif A.lower() == "egg roll":
      card -= 3
    elif A.lower() == "fried chicken":
      card -= 4
    elif A.lower() == "soup":
      card -= 5
    elif A.lower() == "pizza":
      card -= 5
    elif A.lower() == "milk":
      card -= 3
    elif A.lower() == "cheese":
      card -= 4
    elif A.lower() == "butter":
      card -= 4
    elif A.lower() == "yogurt":
      card -= 2
    elif A.lower() == "egg":
      card -= 3
    elif A.lower() == "beef":
      card -= 7
    elif A.lower() == "pork":
      card -= 5
    elif A.lower() == "lamb":
      card -= 8
    elif A.lower() == "chicken":
      card -= 3
    elif A.lower() == "turkey":
      card -= 3
    elif A.lower() == "duck":
      card -= 5
    elif A.lower() == "salmon":
      card -= 4
    elif A.lower() == "shrimp":
      card -= 6
    elif A.lower() == "tuna":
      card -= 6
    print(f'''
    You bought {A}. Your balance on your card is now {card}
          ''')
    receipt.append(A.lower())
    continue
  elif A.lower() == "ask":
    print('''The sections are:
    Produce
    Deli
    Dairy
    Meat


    Type a section to know what you can get

    ''')
    continue
  elif A.lower() == "produce":
    print('''The produce sections are:
    Fruit
    Veggies

    Type a section to know what you can get

    ''')
    continue
  elif A.lower() == "deli":
    print('''The deli sections are:
    Sandwich
    Meal

    Type a section to see the product's inside

    ''')
    continue
  elif A.lower() == "dairy":
    print('''The dairy foods are
    Milk
    Butter
    Yougurt
    Egg
    Cheese

    Type a dairy product to buy.

    ''')
    continue
  elif A.lower() == "meat":
    print('''The meats are:
    Fresh meat
    Poultry
    Seafood

    Type a section to know what you can get.

    ''')
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

    Type a sandwich to buy

    ''')
    continue
  elif A.lower() == "meal":
    print('''The meals are:
    Egg roll
    Fried chicken
    Soup
    Pizza

    Type a meal to buy it

    ''')
    continue
  elif A.lower() == "fresh meat":
    print('''The fresh meats are:
    Beef
    Pork
    Lamb

    Type a product to buy it

    ''')
    continue
  elif A.lower() == "poultry":
    print('''The poultry are:
    Chicken
    Turkey
    Duck

    Type a poultry product to by it

    ''')
    continue
  elif A.lower() == "seafood":
    print('''The seafood are:
    Salmon
    Shrimp
    Tuna

    Type a seafood product to buy it

    ''')
    continue
  elif A.lower() == "quit":
    print("")
    print("You left the supermarket")
    print("")
    print("Your receipt:")
    print("")
    for item in receipt:
      print(f"-{item}")
    print("")
    print("Thank you for shopping with us")
    break
  else:
    print("")
    print('''Invalid input:

    -No spacebar

    -You may have misspelled

    -Put the word the exact way listed''')
    print("")
    continue
else:
  print("")
  print("You have ran out of balance")
  print("")
  print("Your receipt:")
  print("")
  for item in receipt:
    print(f"-{item}")
  print("")
  print("Thank you for shopping with us")
