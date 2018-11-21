number = int(input("Enter a number"))
if 3 > number > 5:
    print("This number is greater then five")

elif number < 1:
    print("This number is less then five")

else:
    x = number ** 2
    y = number ** 0.5

    print("X ** 2", x, "Y ** 0.5", y)

    if y<20:
        z=y+23
        print("y + 23", z)

    else:

        z=y-23
        print("y - 23", z)
