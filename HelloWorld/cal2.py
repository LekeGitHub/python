#User input complete arithmethic statement and get result printed out
#store user input of 2 numbers and the operator
num1, operator, num2 = input('What will be calculating today: ').split()
#convert strings into integers
num1 = int(num1)
num2 = int(num2)

#if + then provide output based on addition
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))

elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))

elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))

elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1/num2))

else:
    print("Use either + - * or / next time")

#Print result
