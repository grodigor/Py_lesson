# 4. Дан список случайных целых чисел. Замените все нечетные числа списка нулями. И выведете их количество.
import random
list_ = [random.randint(1, 100) for i in range(random.randint(1, 100))]
print(list_)
new_list = []

for num in list_:
    if num % 2 == 0:
        num = 0
        new_list.append(num)

print(new_list)
print(f'Четных чисел: {new_list.count(0)}')