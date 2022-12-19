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


# dictionary = {}    # \ - печетаем с новй строки
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

# list1[0] = 123     # меняет значения в сисках

# list2 = list1

# list2[1] = 333    # меняет значения в сисках

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)


# # print(len(list1))        # len показывает длину списка
# # print(list1.pop())       # pop удаляет последние значение
# # print(list1)

# # print(len(list1))
# # print(list1.pop(2))      # pop(2) удаляет 2 е значение значение
# # print(list1)
# # --------


# print(list1.insert(2,11))    # insert(2,11))  - добавляет в множество (после 3 множество, значение 11)
# print(list1)

# print(list1.append(11))    # append(11)  - добавляет в множество (в конец значение 11)
# print(list1)
