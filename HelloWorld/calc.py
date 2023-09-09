#Data Type
#Float: when you are working decimal number e.g 2.1, 2.3.
#Int: are value without decimal

item_price = float(input('Enter price '))
item_count = int(input('item count '))

amount = item_count * item_price
print("Customer spent ", amount)
