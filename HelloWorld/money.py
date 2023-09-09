#putting the values of money and interest
#for ten year interest rate
money = float(input('pls input the amount of invest: '))
interest_rate = float(input('pls input interest rate: '))
#the rate
interest_rate = interest_rate * 0.01
money = money + (money * interest_rate)
for i in range(10):
    print('the ten year interest', money)