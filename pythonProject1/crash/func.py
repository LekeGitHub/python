def add_num(n1, op, n2):
    print("{} {} {} = ".format(n1, op, n2), n1+n2)


def sub_num(n1, op, n2):
    print("{} {} {} = ".format(n1, op, n2), n1-n2)


def mult_num(n1, op, n2):
    print("{} {} {} = ".format(n1, op, n2), n1*n2)


def div_num(n1, op, n2):
    print("{} {} {} = ".format(n1, op, n2), n1/n2)


n1, op, n2 = input("Enter equation: ").split()
n1 = int(n1)
n2 = int(n2)
if op == "+":
    add_num(n1, op, n2)
elif op == "-":
    sub_num(n1, op, n2)
elif op == "*":
    mult_num(n1, op, n2)
else:
    div_num(n1, op, n2)
