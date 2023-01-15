# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# my_list = input(' Введите выражение: ')

# # my_list = '1-2*3'
# my_list = my_list.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').\
#     replace('/', ' / ').split()
# print(my_list)

# if my_list.startswith(' - '):  #почему-то не работает
#     my_list = '-' + my_list[3:]  

# while len(my_list) > 1:
#     while '*' in my_list or '/' in my_list:
#         i = 0
#         while i < len(my_list):
#             if my_list[i] == '*':
#                 my_list[i - 1] = int(my_list[i - 1]) * int(my_list[i + 1])
#                 del my_list[i]
#                 del my_list[i]
#             elif my_list[i] == '/':
#                 my_list[i - 1] = int(my_list[i - 1]) / int(my_list[i + 1])
#                 del my_list[i]
#                 del my_list[i]
#             i += 1

#     while '+' in my_list or '-' in my_list:
#         i = 0
#         while i < len(my_list):
#             if my_list[i] == '+':
#                 my_list[i - 1] = int(my_list[i - 1]) + int(my_list[i + 1])
#                 del my_list[i]
#                 del my_list[i]
#             elif my_list[i] == '-':
#                 my_list[i - 1] = int(my_list[i - 1]) - int(my_list[i + 1])
#                 del my_list[i]
#                 del my_list[i]
#             i += 1
# print(my_list)


# ----------------------------


my_list = input(' Введите выражение: ')

# my_list = '1-2*3'
my_list = my_list.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').\
    replace('/', ' / ')
print(my_list)

my_list = my_list.split()

operation = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y,}

def calculate(operation_1, operation_2):
    i = 0
    while operation_1 in my_list or operation_2 in my_list:
            if my_list[i] in [operation_1, operation_2]:
                my_list[i - 1] = operation.get(my_list[i])(int(my_list[i - 1]))(int(my_list[i + 1]))
                del my_list[i]
                del my_list[i]
            else:
                i += 1

    while len(my_list) > 1:
        calculate('*', '/')
        calculate('+','-')

print(f'{" ".join(my_list)} = {my_list[0]}')