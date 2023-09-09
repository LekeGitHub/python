# Set of data

month = {"January", "Feb", "March", "April", "May"}
print(month)
print(type(month))

# Dictionary
print()
print("____________________________________")
order_list = {"Bread": 340, "Grape": 23, "Town": "London"}
print(order_list)
print(type(order_list))
print("Updating Town from", order_list.get("Town"), "to",
      order_list.update({"Town": "California"}))
order_list.update({"Town": "California"})
print(order_list)

print("Value of of Grape is :", order_list.get("Grape"))

# List
print()
print("____________________________________")
texts = ["Hello", "World", 234, "John", 1900,
         "Gabriel", "Jason", "Sarah"]
print(texts)
print(type(texts))
print(len(texts))
    
# Tuple
print()
print("____________________________________")
tup = ("Hello", "World", 234, "John", 1900,
       "Gabriel", "Jason", "Sarah")
print(tup)
print("Type of tup is :", type(tup))
print("Index 4 : ", tup[4])
print("Tuple slicing from index [3:6]", tup[3:6])
print("Tuple can be printed from back with -value ie tup[-3] is", tup[-3])

# Index & Slicing List
print()
print("____________________________________")
print(texts[1])
print(texts[1:4])

# Append list
print()
print("____________________________________")

texts.append("Adetoroye")
print(texts)

# Reverser list
print()
print("____________________________________")

texts.reverse()
print(texts)

# for loop
print()
print("____________________________________")

for i in tup:
    print(i)

# while loop
print()
print("____________________________________")
i = 0
while i < 8:
    i += 1
    if i == 4:
        continue
    print(i)


