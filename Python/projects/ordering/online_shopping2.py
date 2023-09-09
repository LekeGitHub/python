# This code is to take a food order and process it if the order is part of the food menu
# @menu: is the list of every food present in the resturant
# @order: the user's preference of food

menu = {
    "Banana": 300.00,
    "Eggs": 1000.00,
    "Cakes": 6000.00,
    "Tomatoes": 500.00,
    "Chicken": 1500.00
}

print("Welcome to Zara&Zina Grocery Store!")
print("Here's our menu")
print("______________________")
for item, price in menu.items():
    print(f"{item}: N{price:.2f}")
print("_____________________")

print("Note: If multiple orders, kindly enter them with a space ;)\n"
      "_____________")
order = input("What and what would you like to have today?: ")

if order in menu:
    quantity = int(input(f"How many {order} do you want: "))
    print(f"Great, {quantity} {order} coming up!")
    print(f"That will be N{menu[order]*quantity:.2f}, please.")
    more_order = input("Will that be all?: ").lower()
    if more_order == "yes":
        print("Okay! Thank you for shopping with us.\n"
              "Do have a nice day! :)")
    elif more_order == "no":
        order = input("What more would you like to order: ")

else:
    print("Sorry, we don't have that item on our menu.")
