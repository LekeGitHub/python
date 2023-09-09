# DataBase
# Registration Page

print("Create an account")
fname = input("Enter first name: ")
lname = input("Enter last name: ")

print("Enter your age and Gender: ")
age = input("Enter age: ")
gender = input("Enter gender: ")

print("Create email: ")
email = input("Enter email: ")

print("Create password: ")
password = input("Enter password: ")

print(fname,lname,age,gender, email)

# Login request
print("Login Section Begins \n"
      "....................")
email_check = input("Enter email: ")

# Check if email is correct
while email != email_check:
    print("Couldn't find your account")
    email_check = input("Enter email: ")

# Welcome user
print("Welcome", fname)

# Get user's password
password_check = input("Enter password: ")

# Check if password is correct
while password_check != password:
    print("Wrong password. Try again")
    password_check = input("Enter password: ")

print("Hello ", fname, lname, "\n"
                             "Your are now signed in")

