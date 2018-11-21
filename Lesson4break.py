name = None




while True:
    print("Menu")
    print("1 Enter name")
    print("2 Print greeting")
    print("3 Exit")

    responce = input("Please choose action = ")

    print()

    if responce =="1":
        name = input ("Enter your name: ")
    elif responce == "2":
        if name:
            print("Hello, ", name)
        else:
            print("I dont know your name")

    elif response == "3":
        break
    else:
        print("Incorrect input")