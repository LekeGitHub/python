def login():
    global email, password
    while True:
        email = input("Email: ")
        password = input("password: ")
        if password == reg_password and email == reg_email:
            print(f"Welcome {reg_fn}")
            print("__________________________\n")
        else:
            print("User Not found! Wrong email or password\n"
                  "Try again")
            print("__________________________\n")
            login()


def reg():
    global reg_fn, reg_email, reg_password
    reg_fn = input("Enter your FullName: ")
    reg_email = input("Email: ")
    reg_password = input("Password: ")
    print("Welcome on-board!")
    print("__________________________\n")



choice = input("Login or Signup: ").lower()
if choice == 'login' or choice == 'l':
    login()


elif choice == 'signup' or choice == 's':
    reg()
    print("Now Let's login")
    print("__________________________\n")
    login()
