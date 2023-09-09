# Welcome message

print("Welcome to Quiz game :>)!")

# find out if user will like to play
play_check = input("Would you like to play? : ").lower()

#YES .lower() yes
# Using if condition to check if user does not want to play
if play_check != "yes":
    print("oh okay goodbye! :(")
    quit()

print("Okay! Let us play :>) ")
score = 0

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct you got it right")
    score += 1
else:
    print("Incorrect :>(")

answer = input("What does ATM stand for? ").lower()

if answer == "automated teller machine":
    print("Correct you got it right")
    score += 1
else:
    print("Incorrect :>(")

answer = input("What does LAN stand for? ").lower()

if answer == "local area network":
    print("Correct you got it right")
    score += 1
else:
    print("Incorrect :>(")

answer = input("What does WAN stand for? ").lower()

if answer == "wide area network":
    print("Correct you got it right")
    score += 1
else:
    print("Incorrect :>(")

print("\nYou got " + str(score) + " question(s) correctly")
