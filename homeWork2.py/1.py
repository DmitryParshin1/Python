# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



# my_list = []
# sum = 0

# import random
# for i in range(0, 10):
#         my_list.append(random.randint(1,9))
#         if i % 2 != 0:
#             sum = sum + my_list[i]



# print(my_list)
# print(sum)


# --------------------------------

# list comprehension

from random import randint as RI

my_list = [RI(0,10) for x in range(10) if x%2 !=0]

print(my_list)

def sum(x):
    return 

sum = 0
sum += int(my_list[i])

print(my_list)
print(sum)

