def add_num(nn1, nn2):
    print(f"Sum = {nn1 + nn2}")


def div_num(nn1, nn2):
    print(f"Division = {nn1 / nn2}")


def mult_num(nn1, nn2):
    print(f"Multiplication = {nn1 * nn2}")


def sub_num(nn1, nn2):
    print(f"Subtraction = {nn1 - nn2}")


def module_num(nn1, nn2):
    print(f"Remainder = {nn1 % nn2}")


n1, op, n2 = input("What will you like to calculate? : ").split()
nn1 = int(n1)
nn2 = int(n2)

if op == "+":
    add_num(nn1, nn2)
elif op == "-":
    sub_num(nn1, nn2)
elif op == "*":
    mult_num(nn1, nn2)
elif op == "/":
    div_num(nn1, nn2)
elif op == "%":
    module_num(nn1, nn2)
else:
    print(f"Sorry {op} is not an arithmetic operator sign! Please try again with an appropriate arithmetic sign")