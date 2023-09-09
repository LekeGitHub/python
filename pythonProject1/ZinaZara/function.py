def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


n1, op, n2 = input("Enter arithmetic operation: ").split()

n1 = int(n1)
n2 = int(n2)

if op == '+':
    ans = addition(n1, n2)
    print(ans)

elif op == '/':
    ans = division(n1, n2)
    print(ans)

elif op == '*':
    ans = mult(n1, n2)
    print(ans)

elif op == '-':
    ans = subtraction(n1, n2)