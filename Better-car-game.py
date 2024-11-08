askin = ""
check = 0
print("Type help if you don't know what to do.")
print("")
while askin != "quit":
  askin = input(">")
  if askin.lower() == "start" and check == 1:
    print("The car is already started...")
  elif askin.lower() == "start":
    check = 1
    print("The car has started...")
  elif askin.lower() == "stop" and check == 2:
    print("The car is already stopped")
  elif askin.lower() == "stop":
    print("The car has stopped...")
    check = 2
  elif askin.lower() == "help":
    print("""
    start - to start the car
    stop - to stop the car
    quit - to quit
    """)
  elif askin.lower() == "quit":
    print("You have quit")
    break
  else:
    print("I don't understand that...")
