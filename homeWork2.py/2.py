# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


my_list = []

import random
for i in range(10):
    my_list.append(random.randint(1,9))

print(my_list)


def sum(my_list):
    sum = []
    for i in range((len(my_list)+1)//2):
        sum.append(my_list[i] * my_list[len(my_list) - 1 - i])
    return sum

print(sum(my_list))





# def sum(my_list):
#     numbers = 0
#     for i in range(0,len(my_list), 2):
#         numbers += my_list[i]
#     return numbers * my_list[-1]

# print(sum)

