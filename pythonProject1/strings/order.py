text = input("Convert to acronym : ").upper()

List_text = text.split()

for each_word in List_text:
    print(each_word[0], end="")