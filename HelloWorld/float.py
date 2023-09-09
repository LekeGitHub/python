
money = float(input('How much would you like to invest : '))
interest_rate = float(input('Enter interest rate '))
year = int(input('How many years of investment? '))

interest_rate = interest_rate * 0.1

for i in range(year):
    money = money + (money * interest_rate)

print("Investment after", year, "years : {:.2f}".format(money))
