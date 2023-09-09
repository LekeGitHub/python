def ict(ask):
    print("There will be 5 question to answer in this section")

    # 1st question in ICT

    ans = input("Q1. What is the meaning of ICT? : ").lower()
    if ans == "information communication technology":
        print("Correct!")
    else:
        print("Wrong answer!")

    # 2nd question in ICT

    ans = input("Q2. What is the meaning of RAM? : ").lower()
    if ans == "random access memory":
        print("Correct!")
    else:
        print("Wrong answer!")

# 3rd question in ICT

    ans = input("Q2. What is the meaning of RAM? : ").lower()
    if ans == "random access memory":
        print("Correct!")
    else:
        print("Wrong answer!")


def science (ask):
    print("There will be 5 question to answer in this section")

    # 1st question in ICT

    ans = input("Q1. What is the meaning of ICT? : ").lower()
    if ans == "information communication technology":
        print("Correct!")
    else:
        print("Wrong answer!")

    # 2nd question in ICT

    ans = input("Q2. What is the meaning of RAM? : ").lower()
    if ans == "random access memory":
        print("Correct!")
    else:
        print("Wrong answer!")

    # 3rd question in ICT

    ans = input("Q2. What is the meaning of RAM? : ").lower()
    if ans == "random access memory":
        print("Correct!")
    else:
        print("Wrong answer!")


def maths(ask):
    print("You will be solving some equations")

    # Maths Question 1

    ans = input("Q1. Solve x 25 * x = 100 \n"
                "x = ")
    if ans == "4":
        print("Correct answer")
    else:
        print("Wrong answer")


print("Welcome to summer term Examination")
ask = input("Which of the section will you like to solve first \n"
            "________________________________________ \n"
            "ICT \n"
            "Maths \n"
            "English \n"
            "_________________________________________ \n"
            "Enter your selection: ").lower()

if ask == "ict":
    ict(ask)

if ask == "math" or ask == "mathematics" or ask == "maths":
    maths(ask)