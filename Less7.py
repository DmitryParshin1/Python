# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input(' Введите значение Х: '))
y = int(input(' Введите значение Y: '))

quarter = None

if  x == 0 and y == 0:
    print(' Введие X Y бoльше чем 0')
if x > 0 and y > 0:
    quarter = 1
if x < 0 and y > 0:
    quarter = 2
if x < 0 and y < 0:
    quarter = 3
if x > 0 and y < 0:
    quarter = 4

print(f' Точка с координатами {x} и {y} находится в -> {quarter} четверти ')
