choice = ""
chosen_file = ""
while True:
    

    def saver(folder_file):
        info = str(input("What do you want to save: ")) 
        print("")
        Check = open(f"{folder_file}", "r")
        Checking = Check.read()
        if len(Checking) == 0:
          Saving= open(f"{folder_file}", "w")
          Saving.write(info)
          Saving.close()
          print("Your data has been saved successfully!")
          print("")
        else:
            overwrite = input("Do you want to overwrite the file(y/n): ")
            print("")
            if overwrite.lower() == "y":
              Saving= open(f"{folder_file}", "w")
              Saving.write(info)
              Saving.close()
              print("Your data has been saved successfully!")
              print("")
            elif overwrite.lower() == "n":
              print("Your data has not been saved!")
              print("")

    
    def reader(folder_file):
        Reading = open(f"{folder_file}", "r")
        print("Here is your Data:")
        print("")
        print(Reading.read())
        print("")
        Reading.close()

    
    print("*DataDock*")
    print("")
    choice = str(input("What do you want to do (save, get, quit): "))
    print("")

    if choice.lower() == "save":
      chosen_file = input('''Choose which file you want to save to.
      (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): ''')
      print("")


      if chosen_file == "1":
        saver("DataLog/Data1.txt")
      elif chosen_file == "2":
        saver("DataLog/Data2.txt")
      elif chosen_file == "3":
        saver("DataLog/Data3.txt")
      elif chosen_file == "4":
        saver("DataLog/Data4.txt")
      elif chosen_file == "5":
        saver("DataLog/Data5.txt")
      elif chosen_file == "6":
        saver("DataLog/Data6.txt")
      elif chosen_file == "7":
        saver("DataLog/Data7.txt")
      elif chosen_file == "8":
        saver("DataLog/Data8.txt")
      elif chosen_file == "9":
        saver("DataLog/Data9.txt")
      elif chosen_file == "10":
        saver("DataLog/Data10.txt")
      else:
        print("Invalid choice. Please choose a number between 1 and 10.")
        print("")

    elif choice.lower() == "get":
        chosen_file = input('''Choose which file you want to get from
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): ''')
        print("")

        if chosen_file == "1":
            reader("DataLog/Data1.txt")
        elif chosen_file == "2":
            reader("DataLog/Data2.txt")
        elif chosen_file == "3":
            reader("DataLog/Data3.txt")
        elif chosen_file == "4":
            reader("DataLog/Data4.txt")
        elif chosen_file == "5":
            reader("DataLog/Data5.txt")
        elif chosen_file == "6":
            reader("DataLog/Data6.txt")
        elif chosen_file == "7":
            reader("DataLog/Data7.txt")
        elif chosen_file == "8":
            reader("DataLog/Data8.txt")
        elif chosen_file == "9":
            reader("DataLog/Data9.txt")
        elif chosen_file == "10":
            reader("DataLog/Data10.txt")
        else:
            print("Invalid choice. Please choose a number between 1 and 10.")
            print("")
    elif choice.lower() == "quit":
      print("The progam has been quit.")
      print("")
      print("*DataDock*")
      break
