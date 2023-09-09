
# Acronym Generator

message = input("Enter text to be converted : ")

sep_message = message.split()

for i in sep_message:
    print(i[0], end="")
