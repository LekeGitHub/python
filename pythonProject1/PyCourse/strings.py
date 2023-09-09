
# Dictionary
print()
print("____________________________________")

# Dictionary
order_list = {"Bread": 340, "Grape": 23, "Town": "London"}
print(type(order_list))

# List
order_list_2 = ["Bread", 340, "Grape", 23, "Town", "London"]
print(type(order_list_2))

# Tuple data type
order_list_3 = ("Bread", 340, "Grape", 23, "Town", "London")
print(type(order_list_3))


print(order_list)
print(type(order_list))
print("Updating Town from", order_list.get("Town"), "to",
      order_list.update({"Town": "California"}))
order_list.update({"Town": "California"})
print(order_list)

print("Value of of Grape is :", order_list.get("Grape"))