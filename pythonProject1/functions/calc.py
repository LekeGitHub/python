def add(v1, v2):
    print(f"{v1} + {v2} = {v1 + v2}")


def sub(v1, v2):
    print(f'{v1} - {v2} = {v1 - v2}')


def mult(v1, v2):
    print(f"{v1} * {v2} = {v1 * v2}")


def div(v1, v2):
    print(f"{v1} / {v2} = {v1 / v2:.2f}")


def mod(v1, v2):
    print(f"{v1} % {v2} = {v1 % v2}")


def instruction():
    print("Welcome to Calculator App\n"
          "Enter your arithmetic expression i.e, '2 + 2' if you want to add")


v1, op, v2 = input('Enter your arithmetic expression: ').split()
v1, v2 = int(v1), int(v2)

if op == '+':
    add(v1, v2)
elif op == '*':
    mult(v1, v2)
elif op == '-':
    sub(v1, v2)
elif op == '/':
    div(v1, v2)
elif op == '%':
    mod(v1, v2)
else:
    print("That is not a valid arithmetic :(")
