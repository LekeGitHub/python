# Code gets user's name and store in an empty list
def checkname():
    pass


def getname():
    global name
    name = input("Enter name: ")


# def hello(name):
#     print(f"Hello {name}")


def save(name):
    nameList.append(name)
    print(nameList)


counter = 0
nameList = []
while True:
    getname()
    save(name)
    counter += 1
    if counter > 9:
        print("Sorry that's name we can take.")
        break





