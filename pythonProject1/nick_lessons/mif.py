# Create robotic response system

# Meet Some/ Introduce
print("Hi!, I am a Robot.. and i am pleased to meet you.")

# Ask the user to give the robot a name

robot_name = input("What name will you like to call me? ")

# Thank user for nice name

print("Thank you for naming me", robot_name, " i love it")

# Create and interaction

# Ask for user's name
resp = input("Can i get to know you, please? ").lower()

# check if user want's me to know his/her name
if resp == "yes":
    print("Oh nice!")
    user_name = input("What is your name? ").capitalize()
    print("What a lovely name you have,", user_name)
    fav_sport = input("Well, i will like to know your favorite sport, Mine is football and basketball ").capitalize()
    if fav_sport == "Football":
        print("oh yeah that fantastic, i also like")

else:
    resp = input("Are you shy or did i scary you?: ")
    if resp == "Scare" or resp == "Shy":
        print()