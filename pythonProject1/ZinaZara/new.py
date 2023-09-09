# Get arithmetic expression


num1, op, num2 = input("Enter an arithmetic task : ").split()

num1 = int(num1)
num2 = int(num2)

if op == "+":
    print("Answer is: ", num1 + num2)
elif op == "*":
    print(num1 * num2)