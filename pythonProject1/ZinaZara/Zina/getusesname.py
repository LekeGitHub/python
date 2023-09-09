# Get User's name
import time
def getUserName():
    global userName
    userName = input("Enter your name: ")


def storeName(name):
    global nameList
    nameList.append(name)


count = 0
nameList = []

while True:
    getUserName()
    print(userName)
    storeName(userName)
    print(nameList)
    count += 1
    time.sleep(1)
    if count > 9:
        print("Name list filed up!")
        break