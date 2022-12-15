# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

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

