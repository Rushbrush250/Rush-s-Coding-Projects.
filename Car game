Begin = input(">")
Help = ""
last_input = ""
changed_start = 0

while Help != "quit":
    if Begin == "help" and changed_start == 0:
        Help = input('''
           start - to start the car
           stop - to stop the car
           quit - to exit

           >''')
        changed_start += 1
    else:
        Help = input(">")
        if Help == "start":
            if last_input == "start":
                print("The car is already started.")
            else:
                print("Car started... Ready to go!")
                last_input = "start"
        elif Help == "stop":
            if last_input == "stop":
                print("The car is already stopped.")
            else:
                print("The car has stopped.")
                last_input = "stop"
        elif Help == "quit":
            print("You have quit.")
            break
        else:
            print("I don't understand that...")

    Begin = Help
