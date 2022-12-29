# A. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]


k = int(input(' Введите степень К: '))

equation = {}

import random

for i in range(k, -1, -1):
    equation[i] = random.randint(-100, 100)

print(equation)



def decode(equation: dict) -> str:
    new_equation = []
    for key, value in equation.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' ' + ' + '.join(new_equation) + ' = 0'
    new_equation = new_equation.replace('+ -', '- ').replace('*x**0', '').replace(' 1x', ' x')\
        .replace('-1*x', '-x').replace('x**1', 'x')
    print(f'{new_equation}')


decode(equation)
print(decode(equation))


# eq_str = ''
# for k,v in equation.items():
#     if k == 1:
#         eq_str += f'{v}*x + '
#     elif k == 0:
#         eq_str += f'{v} + '
#     else:
#         eq_str += f'{v}*x**{k} + '
# else:
#     eq_str = eq_str[:-2]

# print(eq_str)




