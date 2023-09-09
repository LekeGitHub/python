# Creating a loging and registration system

# Log System
def login(name, email):
    print("Your name is",name,"and your email is", email)


def reg():
    print("Digital School Registration Page")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    date_ob = input("Day of birth: ")
    month_ob = input("Month of birth: ")
    year_ob = input("Year of birth: ")
    email = input("Enter email: ")
    user_name = input("Enter Username: ")
    pasword = input("Enter password: ")
    return email, pasword, user_name, year_ob, month_ob, f_name, l_name, age, gender


email_check = "adetleke@gmail.com"
password_check = "blablabla"


# Get user details
name = input("Hello welcome to this platform.... What is your name: ")
email = input("Enter your email: ")
password = input("Password: ")


if email == email_check:
    login(name, email)