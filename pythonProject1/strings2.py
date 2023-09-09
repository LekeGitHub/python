programmer = "   programmers love to code   "

print(programmer)

programmer = programmer.lstrip()

print(programmer)
print()
programmer = programmer.rstrip()
print()
print(programmer.capitalize())
print()
print(programmer.upper())

print()

print(programmer.lower())

print()

a_list = ["Bunch", "of", "Random", "words", "stored", "in", "our", "list", "in"]
#           0       1       2       3
print(a_list[3])

for word in a_list:
    print(word)

print("How many 'is' are there in the list? :", a_list.count("in"), " is are there in the list")


