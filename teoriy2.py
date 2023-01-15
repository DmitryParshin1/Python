# ---------------------файлы----------------------

# a - открытие для добавления данных (все данные при запуске будут плюсоваться к старым)
# r - открытие для чтения данных
# w - открытие для записи данных (старые данные удаляются, новые записываются)


# colors = ['red', 'green' , 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors) 
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close

# exit() # не даст строчким ниже запускаться как  код

# ------ 2 способ

# with open('file.txt', 'w') as data:
#     data.write('LINE 2\n')
#     data.write('LINE 3\n')


# -----------------

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()

# этот метод выводит данные из файла в консоль




# ---------------------рекусия----------------------

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1,10):
#     list.append(fib(e))

# print(list)



# ---------------------кортежи----------------------

# a = 3, 4
# print(a)         # запускаем весь кортеж
# print(a[0])      # запускаем первый символ кортежа
# print(a[-1])      # запускаем пследний символ кортежа


# -----------------

# a = 3, 4, 5
# for item in a:
#     print(item)     # печатаем последовательность элементов

# -----------------

#двойное преобразование

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t

# print('r:() g:() b:()'.format(red, green, blue))



# ---------------------словари----------------------


# dictionary = {}    # \ - печетаем с новой строки
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }

# print(dictionary)                # 'up': '↑', 'left': '←', 'down': '↓', 'right': '→'
# print(dictionary['left'])        # ←


# for k in dictionary.keys():
#     print(k)                       # печатает up
#                                         # left
#                                         # down
#                                         # right


# for k in dictionary.values():
#     print(k)                        # печатает ↑
#                                         # ←
#                                         # ↓
#                                         # →


# -----------------



# my_dict = {32:'32', 1:'один', 'ключ': 2142345, 'список': [324, 345, 543, 348]}

# print(my_dict.get(2, 'нет такого ключа'))    # 2 - нет такого ключа
# print(my_dict.get(1, 'нет такого ключа'))    # 1 - один


# my_dict = {32:'32', 3: 45, 1:'один', 'ключ': 2142345, 'список': [324, 345, 543, 348]}

# print(my_dict.get(2,0) + my_dict.get(3,0))        #  45 - будет так как во 2-м ключе нет чисел



# -----------------



# my_dict = {32:'32', 1:'один', 'ключ': 2142345, 'список': [324, 345, 543, 348]}

# # my_dict['NEW'] = 'value'     # добавили новое значение в список
# my_dict[32] = 'value'          # поменяли на друге значение

# print(my_dict)



# -----------------

# my_dict = {}

# num_list = '3409534095840958204368205879054872958908469181394'

# for dig in num_list:
#     my_dict[dig] = my_dict.get(dig, 0) + 1
# print(my_dict)

# {'3': 4, '4': 7, '0': 7, '9': 8, '5': 6, '8': 8, '2': 3, '6': 2, '7': 2, '1': 2}
               
#                прогррамма считает сколько цифр встрречается в строке


# -----------------


# favorite_lanuages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# for name in sorted(favorite_lanuages):                      # sorted - выводит список в алфавитном порядке
#     print(f" \t {name}, thank you for taking the poll! ")


# favorite_lanuages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }

# for lanuages in favorite_lanuages.values():       # values - выведет на экран языки (2-е значения)
#     print(lanuages)

# for lanuages in set(favorite_lanuages.values()):    # set - убирает дубликаты прри выводе
#     print(lanuages)








# ---------------------множество----------------------


# colors = {'red', 'green' , 'blue'}

# colors.add('gray')       # добавляем слово или значение
# print(colors)


# colors.remove('gray')   # удаляет слово или значение
# print(colors)


# colors.discard('gray')   # удаляет слово или значение не вызывая ошибки если нет слова нужного
# print(colors)


# colors.clear()  # очищает все в списке
# print(colors)


# -----------------


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                 # c = {1, 2, 3, 5, 8}  копирует множество а
# u = a.union(b)               # u = {1, 2, 3, 5, 8, 13, 21} - объединяет множество
# i = a.intersection(b)        # i = {8, 2, 5} пересечение множеств
# dl = a.difference(b)         # dl = {1, 3} деление множеств


# q = a\
#     .union(b) \
#     .difference(a.intersection(b))    # q = {1, 21, 3, 13}



# s = frozenset(a)            # замораживает множество и нельзя пользваться вспомогателями





# # ---------------------cписки----------------------


# list1 = [1, 2, 3, 4]

# list1[0] = 123     # меняет значения в списках

# list2 = list1

# list2[1] = 333    # меняет значения в списках

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)


# print(len(list1))        # len показывает длину списка
# print(list1.pop())       # pop удаляет последние значение
# print(list1)

# print(len(list1))
# print(list1.pop(2))      # pop(2) удаляет 2 е значение значение
# print(list1)


# motorcycles = ['honda' , 'yamaha', 'suzuki']
# first_owned = motorcycles.pop(0)              # - пример, если просто pop() - удалит последний элемент в списке
# print(f"The first motorcycles I owned was a {first_owned.title()}")    
# --------

# motorcycles = ['honda' , 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# motorcycles.remove('ducati')     # - удаляет значение по его названию (но только первое, последующие не будут удвлены)
# print(motorcycles)

# --------

# my_list = ['21', '33', 'er', '43', '34rty','11']
# add = '-'

# print(add.join(my_list))       #  21-33-er-43-34rty-11
# print('-'.join(my_list))       #  21-33-er-43-34rty-11  (если без переменной)
 

# --------


# print(list1.insert(2,11))    # insert(2,11))  - добавляет в множество (после 3 множество, значение 11)
# print(list1)

# print(list1.append(11))    # append(11)  - добавляет в множество (в конец значение 11)
# print(list1)

# del - удаляет значение в списке
# del motorcycles[0]         # del  - удалит 0 элемент в списке, значение уже нельзя будет использвать
# print(motorcycles)


# --------

#        sort()

# cars = ['bmw', 'audi', 'subaru', 'mazda', 'toyota']
# cars.sort()              # - сортиует в алфавитном порядке
# print(cars)


# cars.sort(reverse=True)              # - сортиует в обратном от большего к меньшему порядке
# print(cars)

# --------
#        reversed()  - расположение в обратном порядке

# -------------------


# players = ['123', '678', 'qwe', '567', 'fgh', 'cvb']
# print(players[:3])   #  берет только первые 3 элемента  ['123', '678', 'qwe']
# print(players[1:3])    # ['678', 'qwe']
# print(players[-3:])    # ['567', 'fgh', 'cvb']

# for player in players[:3]:
#     print(player.title())
# # 123
# # 678
# # Qwe


# -------------------


# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]     # конструкция [:] сохраняяет список
# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("my favorite foods are:")
# print(my_foods)      #  ['pizza', 'falafel', 'carrot cake', 'cannoli']

# print("\nMy friend's favorite foods are:")
# print(friend_foods)   # ['pizza', 'falafel', 'carrot cake', 'ice cream']


# -------------------



