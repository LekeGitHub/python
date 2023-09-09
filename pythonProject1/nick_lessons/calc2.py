# Get user arithmetic expression

num1, op, num2 = input("Enter a mathematical expression: ").split()
# = input("Enter your age :")

# covert inputted values to integer
num1 = int(num1)
num2 = int(num2)
if op == "+":
    print(num1 + num2)
