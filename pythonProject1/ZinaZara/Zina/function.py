Chat Box

Chat Messages
def message(name):
    print(f"Hello {name}")


# User Name
def getUserName():
    global username
    username = input("What is your name: ")
    return username



getUserName()
message(username)


def hello():
    print("Hello!")


hello()