# This code is to take a food order and process it, if the order is part of the food menu
# @menu: is the list of every food present in the restaurant
# @order: the user's preference of food

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

cart = []

more_orders = True
while more_orders:
    order = input("What would you like to add to your cart?: ").title()

    if order in menu:
        quantity = int(input(f"How many {order} do you want: "))
        print(f"Great, {quantity} {order} added to cart!")
        cart.append(order)
        # print(f"Great, one {order} coming up!")
    else:
        print("Sorry, we don't have that item on our menu.")

    add_more = input("Will that be all?: ").lower()
    if add_more == "yes":
        more_orders = False

print(f"Your orders: {cart}")


#
# if order in menu:
#     print(f"Great, one {order} coming up!")
#
#
