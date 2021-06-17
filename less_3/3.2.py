x = float(input('Enter the number: '))
num = int(str(x).split('.')[1])
print('Decimal part is:', num, '\nFirst digit after point:', num//10)