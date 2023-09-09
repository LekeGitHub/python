print('Hi, welcome to my conversion page '
      '\n Enter the following abbreviations for their measurements'
      '\n Kilogram - Ounce = Kg to O      Milligram - Ounce = M to O       Gram - Ounce = G to O'
      '\n Kilogram - Pound = G to P       Milligram - Pound = M to P       Gram - Pound = G to P' 
      '\n Kilogram - Ton = Kg to T        Milligram - Ton = M to T         Gram - Ton = G to  T'
      '\n kilogram - Milligram = K to M   Milligram - Gram = M to G        Gram - Milligram = G to M'
      '\n kilogram - Gram = Kg to G       Milligram - Kilogram = M to Kg   Gram - Kilogram = G to Kg')

Weight_1, to, Weight_2 = input('From what to what?: ').split()

if Weight_1 == "Kg" and Weight_2 == "O":
    value = float(input('Enter value in Kilogram: '))
    print(value/460, ' ounces')
elif Weight_1 == "Kg" and Weight_2 == "P":
    value = float(input('Enter value in Kilogram: '))
    print(value*0.0018, ' pounds')
elif Weight_1 == "Kg" and Weight_2 == "T":
    value = float(input('Enter value in Kilogram: '))
    print(value/0.83, ' tones')
elif Weight_1 == "Kg" and Weight_2 == "M":
    value = float(input('Enter value in Kilogram: '))
    print(value*0.83, ' milligrams')
elif Weight_1 == "Kg" and Weight_2 == "G":
    value = float(input('Enter value in Kilogram: '))
    print(value*1000000, ' grams')
elif Weight_1 == "M" and Weight_2 == "O":
    value = float(input('Enter value in Milligram: '))
    print(value/1000, ' ounces')
elif Weight_1 == "M" and Weight_2 == "P":
    value = float(input('Enter value in Milligram: '))
    print(value*1000, ' pounds')
elif Weight_1 == "M" and Weight_2 == "T":
    value = float(input('Enter value in Milligram: '))
    print(value/0.83, ' tones')
elif Weight_1 == "M" and Weight_2 == "Kg":
    value = float(input('Enter value in Milligram: '))
    print(value*0.83, ' milligrams')
elif Weight_1 == "M" and Weight_2 == "G":
    value = float(input('Enter value in Milligram: '))
    print(value*1000000, ' grams')
elif Weight_1 == "G" and Weight_2 == "O":
    value = float(input('Enter value in Gram: '))
    print(value/460, ' ounces')
elif Weight_1 == "G" and Weight_2 == "P":
    value = float(input('Enter value in Gram: '))
    print(value*0.0018, ' pounds')
elif Weight_1 == "G" and Weight_2 == "T":
    value = float(input('Enter value in Gram: '))
    print(value/0.83, ' tones')
elif Weight_1 == "G" and Weight_2 == "M":
    value = float(input('Enter value in Gram: '))
    print(value*0.83, ' milligrams')
elif Weight_1 == "G" and Weight_2 == "G":
    value = float(input('Enter value in Gram: '))
    print(value*1000000, ' grams')
elif Weight_1 == "T" and Weight_2 == "O":
    value = float(input('Enter value in Tones: '))
    print(value/460, ' ounces')
elif Weight_1 == "T" and Weight_2 == "P":
    value = float(input('Enter value in Tones: '))
    print(value*0.0018, ' pounds')
elif Weight_1 == "T" and Weight_2 == "Kg":
    value = float(input('Enter value in Tones: '))
    print(value/0.83, ' tones')
elif Weight_1 == "T" and Weight_2 == "M":
    value = float(input('Enter value in Tones: '))
    print(value*0.83, ' milligrams')
elif Weight_1 == "T" and Weight_2 == "G":
    value = float(input('Enter value in Tones: '))
    print(value*1000000, ' grams')
elif Weight_1 == "P" and Weight_2 == "O":
    value = float(input('Enter value in Pounds: '))
    print(value/460, ' ounces')
elif Weight_1 == "P" and Weight_2 == "Kg":
    value = float(input('Enter value in Pounds: '))
    print(value*0.0018, ' pounds')
elif Weight_1 == "P" and Weight_2 == "T":
    value = float(input('Enter value in Pounds: '))
    print(value/0.83, ' tones')
elif Weight_1 == "P" and Weight_2 == "M":
    value = float(input('Enter value in Pounds: '))
    print(value*0.83, ' milligrams')
elif Weight_1 == "P" and Weight_2 == "G":
    value = float(input('Enter value in Pounds: '))
    print(value*1000000, ' grams')
elif Weight_1 == "O" and Weight_2 == "Kg":
    value = float(input('Enter value in Ounces: '))
    print(value/460, ' ounces')
elif Weight_1 == "O" and Weight_2 == "P":
    value = float(input('Enter value in Ounces: '))
    print(value*0.0018, ' pounds')
elif Weight_1 == "O" and Weight_2 == "T":
    value = float(input('Enter value in Ounces: '))
    print(value/0.83, ' tones')
elif Weight_1 == "O" and Weight_2 == "M":
    value = float(input('Enter value in Ounces: '))
    print(value*0.83, ' milligrams')
elif Weight_1 == "O" and Weight_2 == "G":
    value = float(input('Enter value in Ounces: '))
    print(value*1000000, ' grams')
