# Spell the info or terms of how the conversion code works

def instruct():
    print("Welcome to our conversion app\n"
          "kindly select from the conversion options below\n"
          "\n"
          "a. Kilogram to Gram\n"
          "b. Gram to Kilogram\n"
          "c. kilometer to Meter\n"
          "d. Meter to Kilometer\n"
          "........................")

# End of Instruct function

def get_selection():
    option = input("Enter the alphabet of the option you want: ")
    return option

instruct()

option = get_selection()

# Check User's selection
if option == 'a':
    to_convert = float(input("Enter the value in Kilogram: "))
    print(to_convert, "Kilogram = ", to_convert * 1000, "Gram")

elif option == 'b':
    to_convert = input("Enter the value in Gram: ")

elif option == 'c':
    to_convert = input("Enter the value in Kilometer: ")

elif option == 'd':
    to_convert = input("Enter the value in Meter: ")

