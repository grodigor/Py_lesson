# 4. Дан список случайных целых чисел. Замените все нечетные числа списка нулями. И выведете их количество.
import random
def replace_(list_, value = 0):
    return [value if not i % 2 else num for i, num in enumerate(list_)]


new_list = [random.randint(1, 999) for num in range(random.randint(1, 30))]
new_list = replace_(new_list)
print(new_list.count(0))