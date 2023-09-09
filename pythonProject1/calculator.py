#User aritmethic calculation

#Get user aritmethic statement
num1, operator, num2 = input('What would you like to calculate: ').split()

#convert strings to integers

num1 = int(num1)
num2 = int(num2)

#print(num1, operator, num2)
#If operator entered is * then

if operator == "+":
    print(f'{num1} + {num2} = {num1+num2}')

elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))

elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1/num2))

