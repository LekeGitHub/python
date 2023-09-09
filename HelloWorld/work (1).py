

print('Welcome to converting.com'
        '\n in order to convert enter '
      '\n enter kg to g to convert'
      '\n enter g to kg to converts'
      '\n enter mg to g to convert'
      '\n enter g to mg to convert')

currency_1, to, currency_2 = input('convert from what to what').split()

if currency_1 == 'kg' and currency_2 == 'g':
     num = float(input('pls put kg amount'))
     print('N', num*1000)

elif currency_1 == 'g' and currency_2 == 'kg':
     num1 = float(input('pls put g amount'))
     print('N', num1/1000)

elif currency_1 == 'mg' and currency_2 == 'g':
    num = float(input('pls put mg amount'))
    print('N', num/1000)

elif currency_1 == 'g' and currency_2 == 'mg':
    num = float(input('pls put g amount'))
    print('N', num*1000)