#---[ Exercises-1 : Weight Conversion]

weight = int (input('Weight: '))
unit =  input('(K)g or (L)bs: ')

if unit.upper() == "K":
    converted = weight / 0.45
    print(f'Weight in Lbs: {converted}')
else:
    converted = weight * 0.45
    print(f'Weight in Kgs: {converted}')


#---[ Exercises-2 : ]
