
def ask_for_name():
    global name
    name = input("What is your name? ")


def greet(name):
    print("Hello", name)


ask_for_name()
greet(name)