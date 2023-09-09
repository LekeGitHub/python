
print('Hi, welcome to my conversion page '
      '\n To convert Naira to Dollar, enter "N to $"'
      '\n To convert Dollar to Naira, enter "$ to N"'
      '\n To convert Dollar to Naira, enter "N to £"'
      '\n To convert Dollar to Naira, enter £ to N'
      '\n To convert Dollar to Naira, enter $ to £'
      '\n To convert Dollar to Naira, enter £ to $')

currency_1, to, currency_2 = input('From What to What? : ').split()

if currency_1 == "N" and currency_2 == "$":
    value = int(input('Enter value in Naira '))
    print('$', value/460)
elif currency_1 == "$" and currency_2 == "N":
    value = int(input('Enter value in Dollars '))
    print(value*460)
elif currency_1 == "N" and currency_2 == "£":
    value = int(input('Enter value in Naira '))
    print(value/0.0018)
elif currency_1 == "£" and currency_2 == "N":
    value = int(input('Enter value in Pounds '))
    print(value*0.0018)
elif currency_1 == "$" and currency_2 == "£":
    value = int(input('Enter value in Dollars '))
    print(value/0.83)
elif currency_1 == "£" and currency_2 == "$":
    value = int(input('Enter value in Pounds '))
    print(value*0.83)


