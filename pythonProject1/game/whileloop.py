score = "boy"
gender = input("Male of female : ").lower()

while gender == "male":
    score = 0
    print("Welcome to ...")
    play = input("Like to play? : ").lower()
    if play == "no":
        print("okay bye!")
        break
    print("oh nice let us play")
    ans = input("What does CPU stand for? : ").lower()
    if ans == "central processing unit":
        print("Hurray! Correct")
        score += 1
    else:
        print("oh sorry, wrong answer")

    ans = input("What does WAN stand for? : ").lower()
    if ans == "wide area network":
        print("Hurray! Correct")
        score += 1
    else:
        print("oh sorry, wrong answer")

    print("you got " + str(score) + " question(s) correctly")
    continue
