year = int(input('Введите год: '))
if year % 4 == 0 and year % 400 != 0:
    print('YES')
else:
    print('NO')