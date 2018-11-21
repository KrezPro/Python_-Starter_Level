for i in range(2,10,3):
    print("i= ", i)

    for attempts_left in range(3,0,-1):
        password = input("Enter your password "
                         "(you have {} attempts left): ".format(attempts_left))
        if password == "rjcbyec60":
            print("Access granted")
            break

    else:
        print("access denied")