def ict(question):
    print("ICT Questions \n"
          "Answer all 3 questions")

    # Question 1
    ans = input("What is the meaning of ICT : ").lower()
    if ans == "information communication technology":
        print("Correct answer")
    else:
        print("Wrong answer")

    # Question 2
    ans = input("What is the meaning of RAM : ").lower()
    if ans == "random access memory":
        print("Correct answer")
    else:
        print("Wrong answer")

    # Question 3
    ans = input("What is the meaning of ISP : ").lower()
    if ans == "internet service provider":
        print("Correct answer")
    else:
        print("Wrong answer")


def science(question):
    print("SCIENCE Questions \n"
          "Answer all 3 questions")

    # Question 1
    ans = input("What is the meaning of H20 : ").lower()
    if ans == "water":
        print("Correct answer")
    else:
        print("Wrong answer")

    # Question 2
    ans = input("What is the meaning of C02 : ").lower()
    if ans == "carbon-dioxide" or ans == "carbon dioxide":
        print("Correct answer")
    else:
        print("Wrong answer")

    # Question 3
    ans = input("What is the meaning of ISP : ").lower()
    if ans == "internet service provider":
        print("Correct answer")
    else:
        print("Wrong answer")


print("Welcome to summer term Examination")
ask = input("Which of the section will you like to solve first \n"
            "________________________________________ \n"
            "ICT \n"
            "Maths \n"
            "English \n"
            "Science \n"
            "_________________________________________ \n"
            "Enter your selection: ").lower()

if ask == "ict":
    ict(ask)

if ask == "science" or ask == "sci":
    science(ask)
