# A code that prints order and calculate how many

Order_list = ["Burger: $20", "Ketchup: $5", "Chicken: $35"]

# Welcome
print("Wellcome to McDonals, What would you like to order\n"
      "................\n"
      "Order List")

# Print Order
for food in Order_list:
    print(food)

# Getting order
print(".................")
order_choice = input("Can i get your order please: ").capitalize()
if order_choice == "Burger" or order_choice == "Chicken" or order_choice == "Ketchup":
    print("Order Available")
    amount_choice = int(input("How many piece are you getting: "))
    if order_choice == "Burger":
        print("That will be $",amount_choice * 35)
    elif order_choice == "Chicken":
        print("That will be $",amount_choice * 20)
    elif order_choice == "Ketchup":
        print("That will be $",amount_choice * 5)
else:
    print("Not available!")

# Let's create conditions


