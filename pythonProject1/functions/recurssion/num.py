def morning_greetings(time, name):
    print("Good morning", format(name))


def afternoon_greetings(time, name):
    print("Good afternoon", format(name))


name = input("Enter your name: ")
time = int(input("Whats say the time :"))

if time >= 6 and time <= 12:
    morning_greetings("6am", name)
elif time <= 5 and time > 12:
    afternoon_greetings(7, name)
else:
    print("Enter accurate details")
