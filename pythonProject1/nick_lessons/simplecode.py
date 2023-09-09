money = input("THis is my cozy home, will you like some tea?").lower()
if money == "no" or money == "no thank you" or money == "...":
    like = input("Oh Why? or do you prefer pizza? :").lower()
    if like == "yes" or like == "oh yeah" or like == "oh yeah of cause":
        print("okay, i'm gonna place order for pizza.")
    else:
        print("Okay, i guess you don't want anything")
else:
    kind_of_tea = input("Do you like your tea cold or warm: ")
    if kind_of_tea == "warm":
        print("Okay!, warm tea is coming up.")
    else:
        print("Cold tea shall be serve.")
