def naira_dollar(ntd):
    ntd = int(ntd)
    print(ntd/500)


def dollar_naira(dtn):
    dtn = int(dtn)
    print(dtn*500)


print('Hi, welcome to my conversion page '
      '\n To convert Naira to Dollar, enter N to $'
      '\n To convert Dollar to Naira, enter $ to N'
      '\n To convert Dollar to Naira, enter N to £'
      '\n To convert Dollar to Naira, enter £ to N'
      '\n To convert Dollar to Naira, enter $ to £'
      '\n To convert Dollar to Naira, enter £ to $')


resp = input("Please enter the currency you are convert: ")

if resp == "N to $":
    ntd = input("Enter the amount in naira you'll ike to convert to dollar: ")
    naira_dollar(ntd)