# Register and Login

# Registration
def reg():
    global reg_name, reg_password, reg_email
    reg_name = input("Enter your name: ")
    reg_email = input("Enter email: ")
    reg_password = input("Enter password: ")
    print(f"Hello {reg_name}, you are now registered as a user")
    print("________________")


# reg()
def login():
    print("Please enter your email and password to login!")
    email = input("Enter email: ")
    password = input("Enter password: ")

    while password != reg_password and email != reg_email:
        email = input("Enter email: ")
        password = input("Enter password: ")
        if password != reg_password and email != reg_email:
            print(f"Hello {reg_name}, you have successfully logged in! :)")
            break
        else:
            print("Sorry User not found or you've entered a wrong password. \n please try again! ")



    # else:
    #     print("Sorry, User not found")

reg()
login()