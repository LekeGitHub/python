menu_list = ["Banana", "Egg", "Apple", "Bread", "Chicken"]

menu = {"Burger": 2000.00,
        "Fries": 1000.00,
        "Pizza": 6000.00,
        "Salad": 500.00,
        "Chicken": 1500.00}


for item, price in menu.items():
    print(f"{item}: N{price:.2f}")
