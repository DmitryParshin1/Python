# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

import model
import view


def start():
    numbers = input('\n Введите выражение: \n')
    print(view.new_list)
    return numbers

def summa():
    return view.sum

