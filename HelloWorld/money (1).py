#putting the values of money and interest
#for ten year interest rate
money = float(input('pls input the amount of invest: '))
interest_rate = float(input('pls input interest rate: '))
time = int(input('pls put years'))
#the rate
interest_rate = interest_rate * 0.01
for i in range(time):
    money = money + (money * interest_rate)
    print("Investment after", time, "years : {:.2f}".format(money))