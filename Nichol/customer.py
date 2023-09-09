# Get Customer's name and print them out using dictionary
# First let's ask if customer want to enter their name.
customerName = []
def confirm():
    global choice
    choice = input("Enter Customer (Yes/No): ")


def getname():
    global fname, lname
    fname, lname = input("Enter Customer Name: ").split()


def store(fname, lname):
    customerName.append({'fname' : fname, })



while True:
    choice = input("Enter Customer (Yes/No) :").lower()
    if choice == "yes" or choice == "y":
        fname, lname = input("Enter Customer Name: ").split()
        customerName.append({'fname': fname, 'lname': lname})
    elif choice == 'n' or choice == "no":

        for k, v in customerName.items():
            print(k, v)
            break



