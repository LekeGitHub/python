menu_a = {
    "Burger" : 30.00,
    "Bread" : 20.00,
    "Tomatoes": 10.00,
    "Spaghetti": 20.00

}

menu_b = [
    "Burger",
    30.00,
    "Bread"
]

for item, price in menu_a.items():
    print(f"{item}: {price}")

    # 1st loop: item = Burger, price = : 30.00
    # 2nd loop: item = Bread, price = : 20.00
    # 3rd loop: item = Tomatoes, price = : 10
    # 4th loop: item = spaghetti, price = : 20.00
    # END loop
    # for food, price in menu.items():

