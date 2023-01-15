# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# my_list = []

# n = int(input(' Введите число: '))

# sum = 0

# for item in range(1, n+1):
#     number = round(((1 + 1/n)**n), 2)
#     sum += number
#     my_list.append(number)

# print(f' для n чисел -> {my_list}')
# print(sum)

# -------------------------------------


number = int(input(' Введите число: '))

my_list = []

for n in range(1, number + 1):
    num = round((1 + 1/n)**n, 2)
    my_list.append(num if num != int(num) else int(num))

print(f' при n = {number} список ->', end='')
print(*my_list, sep=', ')
print(f' Сумма -> {sum(my_list)}')


# number = int(input('введите число: '))

# list = []

# for item in range(1, number + 1):
#     list.append(round((1 + 1/number)**number, 2))

# print(f'Для n={number} список будет {list}')
# print(f'сумма будет равна: {sum(list)}')
