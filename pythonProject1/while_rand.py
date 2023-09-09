import random

random_num = random.randrange(1, 10)

while True:
    guess = int(input("Guess a random number between 1 - 10 : "))
    if guess == random_num:
        print("You got it")
        break
    else:
        print("Try again")
