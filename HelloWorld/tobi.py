
print('Welcome to converting.com'
        '\n in order to convert enter '
      '\n enter "N to $" to convert from naira to dollar'
      '\n enter "$ to N" to convert from dollar to naira'
      '\n enter "N to E" to convert from naira to Euro'
      '\n enter "E to N" to convert from euro to naira')

currency_1, to, currency_2 = input("Convert from what to what: ").split()

if currency_1 == '$' and currency_2 == 'N':
    num = float(input('How much dollar do you want to convert to naira: '))
    print('N', num/0.0022)

elif currency_1 == 'N' and currency_2 == '$':
     num = float(input('pls put naira amount amount'))
     print('N',num*0.0022)

elif currency_1 == 'E' and currency_2 == 'N':
    num = float(input('pls put naira amount'))
    print('N',num/0.0020)

elif currency_1 == 'N' and currency_2 == 'E':
    num = float(input('pls put euro amount'))
    print('N',num*0.0020)
