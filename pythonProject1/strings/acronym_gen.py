acronym = input("Enter some text: ").upper()

acronym_list = acronym.split()
for i in acronym_list:
    print(i[0], end="")

print()