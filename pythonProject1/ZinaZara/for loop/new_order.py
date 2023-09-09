import time

menu = {"Burger": 2000.00,
        "Fries": 1000.00,
        "Pizza": 6000.00,
        "Salad": 500.00,
        "Chicken": 1500.00}

print("Welcome to Zara&Zina Restaurant!")
print("Here's our King's menu")
print("______________________")

for item, price in menu.items():
    print(f"{item}: N{price:.2f}")
print("_____________________")

cart = { }
counter = 0

while True:
    time.sleep(2)
    order = input("What would you like to add to your cart?: ").title()

    if order in menu:
        quantity = int(input(f"How many {order} do you want: "))
        print(f"Great, {quantity} {order} added to cart!")
        cart.update({quantity: order})
    else:
        print("Sorry, we don't have that item on our menu.")

    add_more = input("Will that be all?: ")
    if add_more.casefold() == 'yes':
        break
    counter += 1

print("_____________________")
print("You ordered")
print(f"While Loop run {counter} time")

# print(cart)

for item, quantity in cart.items():
    print(f"{item}: {quantity}")

print("_____________________")
# comfirm_orders: str = input("Please confrim your orders: ")