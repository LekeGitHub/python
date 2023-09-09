# This is a python about examinations app.
# It asks student bunch of questions and check if they are correct with the stored answer.

print("Welcome to Mr. Leke's Mid Examination App\n"
      "..........................\n"
      "Their will be 3 categories of questions\n")

# Get user's exam choice
choice = input(""
               "a. ICT\n"
               "b. Science\n"
               "c. English\n"
               "\n"
               "Select from the options above: ").lower()

# Check User's choice of exam
if choice == "ict" or choice == 'a':
    print("INSTRUCTION: Answer all Question in this section \n"
          "Each questions carries 2 marks")
    ict_score = 0
    # ICT Question 1
    answer = input("What is ICT: ").upper()

    if answer == "INFORMATION COMMUNICATION TECHNOLOGY":
        print("Yeah Correct!")
        ict_score += 2
    else:
        print("Sorry! Wrong answer")

    # ICT Question 2
    answer = input("What is the meaning of RAM: ").lower()
    if answer == "random access memory":
        print("Yeah Correct")
        ict_score += 2
    else:
        print("Sorry! Wrong answer.")

    # ICT Question 3
    answer = input("What is a podcast: \n"
                   "a. A podcast is an audio recording available over the internet that can downloaded and play on a "
                   "digital device\n"
                   "b. A podcast is a video recording available over the internet that can downloaded and play on a "
                   "digital device\n"
                   "c. A podcast is an audio recording available over the internet that can downloaded and play on a "
                   "device\n"
                   "Which is the correct answer, a, b or c: ")
    if answer == 'a' or "A podcast is an audio recording available over the internet that can downloaded and play on " \
                        "a digital device":
        print("Yeah, that's Correct")
        ict_score =+ 2
    # ICT QUESTIONS COME UP HERE

#elif choice == "science" or 'b':

    # Science Questions in here

#elif choice == "english" or 'c':
    # English question comes in here

