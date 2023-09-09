import random
import math

randList = ["strings", 1.234, 28]

onToTen = list(range(10))

print(onToTen)

randList = randList + onToTen

print(randList)

print(randList[0])

print("List length: ", len(randList))

first3 = randList[0:3]

print(first3)

for i in first3:
    print(f"{first3.index(i)} : {i} ")

print(first3[0] * 3)

print("String" in first3)

print("Index of string : ", first3.index("strings"))