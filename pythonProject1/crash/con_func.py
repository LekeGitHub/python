def currency_converter(currency, value):
    value = int(value)
    if currency == "n to $":
        print(value / 700)
    elif currency == "$ to n":
        print(value * 700)
    elif currency == "n to £":
        print(value / 750)
    elif currency == "£ to N":
        print(value * 750)


print('Hi, welcome to your favorite currency converter'
      '\n_________________________________________'
      '\n To convert Naira to Dollar, enter N to $'
      '\n To convert Dollar to Naira, enter $ to N'
      '\n To convert Dollar to Naira, enter N to £'
      '\n To convert Dollar to Naira, enter £ to N'
      '\n To convert Dollar to Naira, enter $ to £'
      '\n To convert Dollar to Naira, enter £ to $'
      '\n_________________________________________'
      '\n')

currency = input("Please enter the currency you are convert: ")
value = input("Enter the amount in naira you'll ike to convert to dollar: ")

currency_converter(currency, value)