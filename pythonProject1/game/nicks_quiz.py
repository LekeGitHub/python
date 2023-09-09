print("Hey Hello!")

response = input("Will you like to test your knowledge? ").lower()

if response != "yes" and response != "yeah" and response != "yeh":
    print("oh! Goodbye :(")
    quit()

score = 0
print("Oh nice, Let's play ;)")
answer = input("ROM stand for : ").lower()

if answer == "read only memory":
    print("Yeah! correct :)")
    score += 1

else:
    print("Wrong answer :(")

print("Your score is ", score, "\n")
answer = input("RAM stand for : ").lower()

if answer == "random access memory":
    print("Yeah! correct :)")
    score += 1

else:
    print("Wrong answer :(")
print("Your score is ", score, "\n")