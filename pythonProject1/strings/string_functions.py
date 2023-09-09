rand_strings = "   hello world     "
print(rand_strings)
rand_strings = rand_strings.lstrip()
print(rand_strings)
rand_strings = rand_strings.rstrip()
print(rand_strings)

print(rand_strings.capitalize())
print(rand_strings.upper())
print(rand_strings.lower())

a_list = ["bunch", "of", "random", "words"]
print(" ".join(a_list).capitalize())

a_list_2 = rand_strings.split()
for i in a_list_2:
    print(i)

print("how many he :", rand_strings.count("he"))

print("Where is world :", rand_strings.find("world"))

print(rand_strings.replace("world", "dear, and how are you?"))
