def solve_eq(equation):


    x, operator, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)

    if operator == "+":
        return x + " = " + str(num2 - num1)
    elif operator == "-":
        return "x = " + str(num2+num1)
    elif operator == "/":
        return "x = " + str(num2 + num1)

equation = input("Enter an equation : ")

equation = equation.replace(" ", "")
print(solve_eq(equation))