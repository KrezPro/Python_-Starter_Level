def outer_function():
    var = 8  # создание локальной переменной var

    def inner_function():
        # указывает, что необходимо использовать переменную из внешней функции
        nonlocal var
        print(var)  # 8
        var = 10

    print(var)  # 8
    inner_function()  # вызов внутренней функции
    print(var)  # 10


# создание глобальной переменной var
var = 0
print(var)  # 0
outer_function()
print(var)  # 0


print("     /////////////           ")

def outer_function2():
    var2 = 8  # создание локальной переменной var

    def inner_function2():
        # указывает, что необходимо использовать глобальную переменную
        global var2
        print(var2)  # 0
        var2 = 10

    print(var2)  # 8
    inner_function2()  # вызов внутренней функции
    print(var2)  # 8


# создание глобальной переменной var
var2 = 0
print(var2)  # 0
outer_function2()
print(var2)  # 10