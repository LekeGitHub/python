# List Types

# 1 List
a = [1, 2, -3, 4, 5]

# to add elements to the list
a.append(1)
print(a)

# Let's append strings to our "a" list
a.append("hello")
print(a)

# We can also add a new list to the "a" list
a.append(["Garri", "Potatoes"])

# to delete an elements from the list
a.pop()
print(a)

# Notice pop always deletes the last element of the list
a.pop()
print(a)

# We can also delete a specific data by targeting it's index
a.pop(5)  # in this line we are deleting the element in index 5
print(a)

# We can change any elements in the list
a[0] = 100
print(a)

# Lenght of list
print(len(a))