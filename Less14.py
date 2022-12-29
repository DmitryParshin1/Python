# 32*x**2 + 4*x -6 = 0
# A*x**2 + B*x -C = 0

# my_string = 'Питон самый лучший в мире язык'

# new_string = my_string.split()
# new_string2 = my_string.split('и')
# new_string3 = my_string.replace('и', '$').replace('а', '')


# my_string = '32*x**2 + 4*x -6 = 0'

# new_string = my_string.replace('*x', '').replace('**2', '').replace('= 0', '').replace('+', '').replace('- ','-')
# # .replace(' ', '')
    
# print(new_string)

# my_list = new_string.split()

# print(my_list)

# for i in range(len(my_list)):
#     my_list[i] = int(my_list[i])

# print(my_list)

# from math import sqrt

# def qwerty(a,b,c):
#     d = b ** 2 - 4 * a * c
#     x_1 = (-b + sqrt(d)) / a * 2
#     x_2 = (-b - sqrt(d)) / a * 2
#     return d,x_1,x_2

# print(qwerty(my_list[0], my_list[1], my_list[2]))


# ---------------------------------

# 2 - й вариант
# не работатет

equation = '32*x**2 + 4*x - 6 = 0'

def create_koef(equation: str) -> tuple:
    new_koef = []
    nq = equation.replace(' ', '').replace('=0', '')\
        .replace('+', ' ').replace('-', ' -').split()
    for item in nq:
        new_koef.append(int(item.split('*x')[0]))
    return new_koef

create_koef(equation)

import match

def solution(koef: list):
    a, b, c = koef
    disc = b**2 - 4*a*c
    if disc > 0:
        x1 = (-b + match.sqrt(disc))/(2*a)
        x2 = (-b - match.sqrt(disc))/(2*a)
        return x1, x2
    elif disc ==0:
        x = -b/ (2*a)
        return x
    else:
        return None

print(solution(create_koef(equation)))
