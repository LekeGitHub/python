# First we will display instruction about the conversion
def instruction():
    print("Welcome to conversion.com"
          "\n in order to convert,"
          "\n enter kg to g to convert"
          "\n enter g to kg to converts"
          "\n enter mg to g to convert"
          "\n enter g to mg to convert")

def get_user_input():
    convert_from, to, convert_to = input("convert from what to what: ").split()
    return convert_from, to, convert_to

instruction()
get_user_input()

# def check_user_input(convert_from, convert_to):
if convert_from == "kg" and convert_to == 'g':
    num = float(input('pls put kg amount'))
    print('N', num*1000)

elif convert_from == 'g' and convert_to == 'kg':
    num1 = float(input('pls put g amount'))
    print('N', num1/1000)

elif convert_from == 'mg' and convert_to == 'g':
    num = float(input('pls put mg amount'))
    print('N', num/1000)

elif convert_from == 'g' and convert_to == 'mg':
    num = float(input('pls put g amount'))
    print('N', num*1000)


