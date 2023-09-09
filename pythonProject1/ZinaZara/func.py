# Learning about functions

# Create a Calculator with function

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2


num1, op, num2 = input("Enter arithmetic expression: ").split()
bn
# Convert st r to int

num1 = int(num1)
num2 = int(num2)

if op == '+':
    ans = add(num1, num2)
    print("Answer =", ans)

elif op == '-':
    ans = sub(num1, num2)
    print("Answer =", ans)