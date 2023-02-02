# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота 'интеллектом'


import random

Welcom = ('На столе лежит 300 конфет. Играют два игрока делая ход друг после друга.\n'
          'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
          'Все конфеты оппонента достаются сделавшему последний ход.\n')
print(Welcom)

total = 300
player_1 = input(' Введите имя ')
player_2 = input(' Введите имя ')
sum_sweet = 0


number = random.randint(1,2)
# if number == 1:
#     player_1
# else:
#     number == 2
#     player_2


while total > 0:
    if number == 1:
        take = 0
        print(f' Ваш ход {player_1} на столе {total} конфет')
        # sum_sweet = int(input('Сколько конфет вы хотите взять? - '))
        while True:
            try:
                take = int(input('Сколько конфет вы хотите взять?: '))
                if 0 < sum_sweet < 29:
                    break
            except ValueError:
                    print(' взять можно только от 1 до 28 конфет \n')
        total = total - sum_sweet
        if total > 0:
            player_2
            print(f' осталось еще {total} конфет ')
        else:
            print(' конфеты кончилсь ')

    if number == 2:
        print(f' Ваш ход {player_2} на столе {total} конфет')
        sum_sweet = int(input('Сколько конфет вы хотите взять? - '))
        while sum_sweet > 28 or sum_sweet < 0 or sum_sweet > total:
            print('взять можно только от 1 до 28 конфет')
        total = total - sum_sweet
        if total > 0:
            player_1
            print(f' осталось еще {total} конфет ')
        else:
            print(' конфеты кончилсь ')
