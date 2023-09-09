# Now let's create a question and response

# Get Name User's:
name = input("Enter your name: ")

# Get User's Age

# Get User's email

# Ask user for class

# print out class list
print("Class List!\n"
      "Grade 1\n"
      "Grade 2\n"
      "Grade 3\n"
      "")
student_class = input("What Grade are you: ").lower()

# check for grade and ask question

if student_class == "grade 1" or student_class == " g1" or student_class == "1":
    # Confirm
    confirm = input(f"Hey {name}, are you sure your grade is {(student_class).capitalize()}").lower()
    if confirm == "yes" or confirm == 'y':
        pass #ask questions
    else:
        print("Sorry, you need to go back and select your grade.")

elif student_class == "grade 2" or student_class == " g2" or student_class == "2":
    pass
    # Ask a little hard questions


elif student_class == "grade 3" or student_class == " g3" or student_class == "3":
    pass
    # Ask hard questions

else:
    print("You didn't enter your Class Grade correctly\n"
          "Or you Grade is yet to be captured!")
