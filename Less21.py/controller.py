# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

import model
import view


def start():
    my_list = input('\n Введите выражение: \n')
    return my_list

def numbers():
    return view.new_list

def summa():
    return view.sum


# def click():
#     view.sum