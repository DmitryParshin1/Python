# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# numbers = int(input(' Введите целое число: '))

# a = ' '

# while numbers > 0:
#     a = str(numbers % 2) + a
#     numbers = numbers // 2

# print(a)



# bin() – функция, преобразовывающая целое число в двоичную строку. 
# В качестве параметра принимает десятичное число



# numbers = int(input(' Введите целое число: '))

# a = ' '

# while numbers > 0:
#     a = str(numbers % 2) + a
#     numbers = numbers // 2

# print(a)

 
#  =================================
# map




numbers = int(input(' Введите целое число: '))

a = 0

while numbers > 0:
    a = list(map(str((numbers % 2) + a)))
    numbers = numbers // 2

print(a)