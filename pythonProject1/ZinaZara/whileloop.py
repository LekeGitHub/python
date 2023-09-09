n = 0
while True:
    # A python code that can be used to calculate digits

    # Welcome the user
    print("Welcome to my calculator!\n"
          "Follow the instruction\n")

    # Get numbers from user
    n1 = input("Enter first digit: ")
    op = input("Enter operator sign: ")
    n2 = input("Enter second digit: ")

    # Convert to integer
    n1 = int(n1)
    n2 = int(n2)

    # Check the operator and determine what arithmetic should be done
    if op == "*":
        print("Answer is: ", n1 * n2)
    elif op == "+":
        print("Answer is: ", n1 + n2)

    n += 1
