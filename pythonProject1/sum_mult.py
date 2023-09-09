# Calculate the sum and multiplication of two numbers.

# Get the two numbers and save in num_1 and second number in num_2
num_1, num_2 = input("Enter 2 number with space in between them : ").split()

# print value entered
print("You entered {} and {}".format(num_1, num_2))

# Convert values to integer
num_1 = int(num_1)
num_2 = int(num_2)

# Calculate the multiplication and sum of the two number
print("The sum of the two numbers entered is : {} + {} = {}".format(num_1, num_2, num_1+num_2))
print("The multiplication of the two numbers entered is : {} * {} = {}".format(num_1, num_2, num_1 * num_2))
