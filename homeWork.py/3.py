# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random

my_list = []

for i in range(10):
    my_list.append(i)

print(my_list)

# for i in range(len(my_list)-1, 0, -1):
#         a = random.randint(0, i + 1)
#         my_list[i], my_list[a] = my_list[a], my_list[i]
# print(my_list)

# или 


def my_shuffle(my_list: list):
    new_list = []
    while len(my_list) > 0:
        ni = random.randint(0, (len(my_list) - 1))
        new_list.append(my_list.pop(ni))
    return new_list

print(my_shuffle(my_list))