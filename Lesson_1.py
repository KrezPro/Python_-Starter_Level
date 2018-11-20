
name = input("What is your name?")
print ("Hello,", name)

x = float(input("First number: "))
y = float(input("First number: "))

operation = input("Operation: (+, - , *, /)")

resualt = None

if operation == "+":
    result = x+y
elif operation == "-":
    result = x-y
elif operation == "*":
    result = x*y
elif operation == "/":
    result = x/y

else:
    print ("Unsupportid operation")

if result is not None:
    print("Result:", result)