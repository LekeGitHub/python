# Exam Questions

# Display Category of test
print("Select from the option below")

select = input("a. ICT\n"
               "b. Math\n"
               "c. English\n"
               "Select: ").lower()

# Let's check user's exam choice
if select == 'a' or "ICT":

    ict_score = 0
    # Ask ICT Questions
    answer = input("What is RAM: ").lower()
    if answer == "random access memory":
        print("Yeah correct!")
        ict_score += 2
    else:
        print("Ops! That is a wrong answer")