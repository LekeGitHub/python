letter_z = "z"
num_3 = "3"
a_space = " "  #


def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False


num = input("Enter a num to check : ")
# check = isfloat(num)

# print(check)
if isfloat(num):
    print(f"'{num}' is a float or can be converted to float")
else:
    print(f"'{num}' is not a float and can't be converted to a float")
