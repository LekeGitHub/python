score = 0

while score == 0:
    try:
        number = int(input("Enter a number : "))
        break

    except ValueError:
        print("You didn't enter a number")
    score += 1
    continue

print("Thank you for entering a number.")