# List functions

order_list = []

order_list.append("Banana")  # added banana to my list
print(order_list)

order_list.append("Apple")
print(order_list)

order_list.append("Chicken")
print(order_list)

order_list.append("Tomatoes")
print(order_list)

print(len(order_list))

shopping_list = ["Jeans", "Sneakers", "Perfume"]

order_list.append(shopping_list)

print(order_list)

# How to delete an elements/item in our list
order_list.pop()
print(order_list)

temp = order_list[0]

order_list[0] = order_list[1]

print(order_list)

order_list[1] = temp

print(order_list)

