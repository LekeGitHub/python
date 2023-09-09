print("WELCOME TO MY CODING GAME ;)")

score = 0

play = input("Will you like to play? ").lower()

if play != "yes":
    print("Oh! Okay Bye...")
    quit()
print("Okay! Let's play :) ")
answer = input("What is the full meaning of ICT : ").lower()
if answer != "information communication technology":
    print("Sorry! Wrong answer")
else:
    print("correct")
    score += 1

answer = input("What is the full meaning of RAM : ").lower()
if answer != "random access memory":
    print("Sorry! Wrong answer")
else:
    print("correct")
    score += 1

answer = input("What is the full meaning of CPU : ").lower()
if answer != "central processing unit":
    print("Sorry! Wrong answer")
else:
    print("correct")
    score += 1

answer = input("What is the full meaning of ATM : ").lower()
if answer != "automated teller machine":
    print("Sorry! Wrong answer")
else:
    print("correct")
    score += 1

answer = input("What is the full meaning of LAN : ").lower()
if answer != "local area network":
    print("Sorry! Wrong answer")
else:
    print("correct")
    score += 1

print("You got " + str(score) + " correctly!")
print("You got " + str((score/5) * 100) + "%")
