
name = "Tobi"
a = 3

while True:
    try:
        user_name = input("Enter your username : ")
        password = input("Enter your password 'Pass must be alphanumeric' : ")
        verify_password = input("Re-enter password")

        if password == verify_password:
            print("Password verify")
        break
        else:
        print("not")

    except ValueError:
        print("Kindly enter the right details")

print("Thank you for registering.")
