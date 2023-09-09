# DO simple arithmetic

# Function to get data
def get_data():
    num1, num2 = input("Enter 2 numbers : ").split()

# Get value from user
get_data()

# Check type of data
print("type of data in num1 is ", type(num1), "type of data in num2 is", type(num2))

# Convert from str to int
num1 = int(num1)
num2 = int(num2)

# Check type of data
print(type(num1), type(num2))

num3 = num1 + num2

print(num3)