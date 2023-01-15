# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.

# *Пример:* 

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


# data = '1, 2, 3, 5, 1, 5, 3, 10'.split()

# new_list = []

# for item in range(len(data)):
#     flag = True
#     for j in range(len(data)):
#         if data[item] == data[j] and item != j:
#             flag = False
#             break
#     if flag == True:
#         new_list.append(data[item])
# print(new_list)


# ------------------------------

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# print(my_list)
# for i in my_list:
#     if my_list.count(i) == 1:
#         print(i)


# ------------------------------

import random

my_list = [random.randint(0,10) for i in range(15)]
print(my_list)

new_list = [x for x in my_list if my_list.count(x) == 1]
print(new_list)
