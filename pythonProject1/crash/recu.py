def calc_sum(n):
    if n == 1:
        return 1
    else:
        return n + calc_sum(n-1)
# 1st: is 3 == 1 NO, the it 3 +

sum = calc_sum(10)
print(sum)