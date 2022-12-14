# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))
d = int(input('Введите число D: '))
e = int(input('Введите число E: '))

max = a
if b > max: max = b
if c > max: max = c
if d > max: max = d
if e > max: max = e

print(max)

# еще вариант
# list = [a,b,c,d,e]
# max = list[0]
# for i in list:
#     if i > max:
#         max = i

# print(max)



# еще вариант

# max = -10000000
# list = []
# for i in range(5):
#     number = int(input(('введите число' , i ,': ')))
#     list.append(number)
#     if number > max:
#         max = number

# print(max)



# еще вариант

# my_list = []

# если не нужна переменная i, но нужен цыкл то вместо  ставим _ 

# for i in range(5):
#     number = int(input(f'Введите {i + 1} число: '))
#     my_list.append(number)
#             append - добавляе в конец списка

      
#       max = my_list[0]

# for item in my_list:
#     if item > max:
#         max = item

# print(max)