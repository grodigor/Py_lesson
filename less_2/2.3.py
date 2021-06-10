distance = float(input('Введите длину трассы в километрах: '))
start = 0
v = float(input('Скорость Васи в "км/ч": '))
t = float(input('время в пути: '))
if v > 0:
    stop = start + v * t
    print('До финиша осталось: ', distance - stop, 'км')
elif v < 0:
    stop = start - abs(v * t)
    print('У самурая нет цели, есть только путь. \nДо финиша осталось', distance - stop, 'км')
else:
    print('Вася проснись ты обосрался')
