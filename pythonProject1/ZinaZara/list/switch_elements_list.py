# Let's create a fruits list
fruits_list = ["mango", "apple", "banana"]
print(fruits_list)

# How can we re-arrange in alphabetical order
# 1 we create a temporary place older to store on of the element

temp = fruits_list[0]  # "mango" has been stored in temp
print(temp)

fruits_list[0] = fruits_list[1]  # Move apple to index 0
fruits_list[1] = fruits_list[2]  # Move banana to index 1
fruits_list[2] = temp  # move what's in temp to index 2

print(fruits_list)

# short method

fruits_list[0], fruits_list[2] = fruits_list[2], fruits_list[0]

print(fruits_list)