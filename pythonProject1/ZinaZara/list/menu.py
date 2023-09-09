import time
# This code is to take order and process the order if it is available


menu = {
    "Burger": 300.00,
    "Fries": 500.00,
    "Pizza": 1000.00,
    "Chips": 300.00,
    "Chicken": 2000
}

print("Welcome to Zina and Zara Fast Food!")
print("Here's our food menu")
print("_______________________")

for food, price in menu.items():
    print(f"{food}: N{price:.2f}")
print("_______________________")

order = input("What would you like to have today?: ").title()

if order in menu:
    print(f"Great, one {order} coming up!")
    print(f"That will be {menu[order]:.2f} please.")
else:
    print("Sorry, we don't have that item on our menu list")