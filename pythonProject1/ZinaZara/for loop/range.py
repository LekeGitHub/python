import random

num = random.randrange(1, 10)

guess = int(input("Guess the magic number between 1 and 9?: "))

while guess != num:
    print(f"Oh Oh! Sorry wrong guess the number is {num}")
    guess = int(input("Guess the magic number between 1 and 9?: "))
    if guess == num:
        print(f"Yeah! You guessed right! and magic is {num}")


