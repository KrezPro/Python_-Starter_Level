import Lesson5DefHello

def print_me(limited):
    for _ in range(limited):
        Lesson5DefHello.HelloWorld()
        print(_)

print_me(11)