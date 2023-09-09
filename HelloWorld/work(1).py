# the information about the conversion

print('Trying to convert weight, follow the instructions bellow'
      '\n To convert Milligram  to gram, enter : mg to g'
      '\n To convert Kilogram to gram, enter kg to g'
      '\n To convert Gram to Kilogram  g to kg' 
      '\n mg to kg   kg to mg  g to mg'
      '\n mg to t    kg to t   g to t'
      '\n mg to o    kg to o   kg to o'
      '\n mg to p    kg to p   kg to p')


Weight_1, to, Weight_2 = input('convert from which weight to which weight').split()

if Weight_1 == 'mg' and Weight_2 == 'g':
      num = float(input('pls input mg value: '))
      print(num*0.001)
elif Weight_1 == "g" and Weight_2 == "mg":
      num = float(input('pls input g value'))
      print(num/0.001)
elif Weight_1 == "kg" and Weight_2 == "mg":
      num = float(input('pls input g value'))
      print(num*1000000)
elif Weight_1 == "mg" and Weight_2 == "kg":
      num = float(input('pls input g value'))
      print(num/1000000)
elif Weight_1 == "kg" and Weight_2 == "g":
      num = float(input('pls input g value'))
      print(num*1000)
elif Weight_1 == "g" and Weight_2 == "kg":
      num = float(input('pls input g value'))
      print(num/0.1000)
elif Weight_1 == 'mg' and Weight_2 == 't':
      num = float(input('pls put mg value'))
      print('unknown value')
elif Weight_1 == 'kg' and Weight_2 == 't':
      num = float(input('pls put mg value'))
      print('unknown value');
elif Weight_1 == 'g' and Weight_2 == 't':
      num = float(input('pls put mg value'))
      print('unknown value')
elif Weight_1 == 'mg' and Weight_2 == 'o':
      num = float(input('pls put mg value'))
      print(num/28350)
elif Weight_1 == 'g' and Weight_2 == 'o':
      num = float(input('pls put mg value'))
      print(num/28.35)
