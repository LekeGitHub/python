print("Hello there")
name = input("What is your name? ")
print("Hello ", name)

play = input("Will you like to test your knowledge? : ")

if play != "yes":
    print("Oh Goodbye")
    quit()

answer = input("What is the meaning of ROM? : ")

if answer == "read only memory":
    print("Yeah correct!")
else:
    print("Wrong answer!")