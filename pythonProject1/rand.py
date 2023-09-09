import random

rand_num = random.randrange(1, 10)

guess = int(input("Guess a random number from range 1 - 10 : "))

print("Random number generated is : ", rand_num)

if guess == rand_num:
    print("Yeaah!, Good guess")
else:
    print("Wrong guess, pls try again")
