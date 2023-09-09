# Lists, Bubble Sort, List Comprehension

import random
import math

randList = ["Strings", 123, 1.234]

OneToTen = list(range(10))

randList = randList + OneToTen

print(randList)

first3 = randList[0:3]

print(first3)

for i in first3:
    print("{} : {}".format(first3.index(i), i))
    