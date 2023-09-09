# Task: Create an ordering system that allows user to select
# multiple items from the supermarket shelves and add to their cart,
# you can ask them to delete from their cart or add more items to their cart

# Start by welcome user to store
# and display all you have

print("Welcome message")

menu = ["Banana", "Oranges", "Eggs", "Cakes", "Tomatoes", "Chicken"]
print("Here are the items on the menu")
print("_____________________")
for item in menu:
    print(item)
print("_____________________")
cart = input("Please type in what you'll like to buy: ").split()

for i in cart:

