food_list = {"Burger": 200, "cheese": 30, "Macaroni": 40, "Steak Meat": 50}
print(type(food_list))

print("_________________")
for item, price in food_list.items():
    print(f"{item}: N{price:.2f}")
print("_________________")

order = input("What will you like to order: ").title()

if order in food_list:
    print(f"Great, one {order} coming up!")
    print(f"That will be N{food_list[order]:.2f}, please.")
else:
    print("Sorry, we don't have that item on our menu")