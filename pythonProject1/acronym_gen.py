# Ask for a string
acronym = input("Enter a string : ")

# convert string to uppercase
acronym = acronym.upper()
# Convert to list

acronym_new = acronym.split()
# print(acronym)

# Cycle through the list

for word in acronym_new:
    print(word[0], end="")
print()
