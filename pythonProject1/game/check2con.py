score = 0
answer = input("Select all the possible outcome"
               "\na. we can code with scratch"
               "\nb. we can code python with pycham"
               "\nc. we can write code with powerpoint"
               "\nd. we can program the sky"
               "\nanswer: ")
print(answer)
if answer == "a b" and answer != "c b":
    print("Yeah you are correct")
    score += 1
else:
    print("Oh sorry, that's incorrect or you didn't select all possible outcome")

