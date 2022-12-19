# ---------------------переменные и тип данных---------------------------
# int, float(не целое число), boolean, str, list, None(объявляем перременную без данных)

# value = None
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12345
# print(type(value))

# s = 'привет' - строка
# print(s)

# \n  - переход на новую строку

# print(a, '-',b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# Разные форматы вывода

#----------


# list = [1,2,3,4,] - список (он же массив)
# list = ['1' ,'2' ,'3' ,'4'] - список из строк



# ---------------------ввод данных и вывод----------------------
# print('введие а')
# a = input()

# a = int(input('Введите число А: '))



#print('введие а')
# a = int(input())
#print('введие b')
# b = int(input())
#print(a,' + ' , b, ' = ', a+b)
#чтобы начать вычисления надо присвоить значание int
#float - дробное число


# ---------------------арифметические операции----------------------
#   приориет операций +,-,*,/,%,//,**
#   () скобки меняют приоритет

# a = 5
# b = 7
# c = a + b
# print(c)

# c = a // b - деление в целых числах
# c = a % b - остаток от деление
# c = a ** b - возведение в степень

#----------

# a = 1.3
# b = 3
# c = round(a + b, 5)    где round - окугляет по математической методике
#                         5 - скольк знаков псле запятой показать
# print(c)


#----------

# a = 3
# a = a + 5 
# a += 5 - тоже самое


# ---------------------логические операции----------------------
#   операции > , >= , < , <= , == , != 
#   not, and, or - не путать с   & , | , ^
#   is , is not , in , not in



# a = 1 > 4   
# print(a)     - будет false

# a = 1 < 4 
# print(a)     - будет true

# a = 1 < 4 and 5 > 2
# print(a)     - будет true

# a = 1 == 2   
# print(a)     - будет false

# a = 1 != 2   
# print(a)     - будет true

# a = [1,2]
# b = [1,2]   
# print(a == b)     - будет true

# a = 1 < 4 < 5
# print(a)     - будет true



#----------

# f = 1 > 2 or 4 < 6

# где  or - это ИЛИ

# print(f) - будет true


# f = [1,2,3,4]
# print(f)
# print(2 in f) - будет true так как 2 - содержиться в списке f
# print(2 in f) - будет false  так как not отрицает пррисутствие 2 - содержиться в списке f





# ---------------------управляющие операции----------------------
#   операции if , if - else, while , for


# a = int(input(' a = '))
# b = int(input(' b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


#----------


# username = input(' Введите имя: ')
# if username == ' Маша ':
#     print(' Ура, это Маша')
# elif username == ' Марина ':
#     print(' Я ждал вас, Маррина ')
# elif username == ' Ильнар ':
#     print(' Ильна - топ ')
# else:
#     print(' Привет, ', username)


#----------

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted) - будет перевернутая 32

#----------


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('пожалуй')
#     print('хватит')
# print(inverted) - будет перевернутая 32


#----------

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)
# возвели все в квадрат

#----------

# r = range(10)
# for i in r:
#     print(i)     - получим 1,2,3,4,5,6,7,8,9

# for i in range(1, 10 , 2):
#     print(i)     - получим 2,4,6,8, - нечетные числа




# ---------------------строки----------------------

# text = ' съешь еще этих мягких французских булок '

# print(len(text))                     - 39
# print('еще' in text)                 - true  (наличие строки или слова)
# print(text.isdigit())                - false  (являются символы цифрами)
# print(text.islower())                - true   (являются ли символы - нижнем регистром)
# print(text.replace('еще' , 'ЕЩЕ'))   (заменить одно слово на другое)



#----------

# help(  функцинал  )  - даст определение что за функция
# и что она выполняет

# что бы выйти из текста - клавиша Q

#----------



# ---------------------срезы----------------------


# text = ' съешь еще этих мягких французских булок '

# print(text[0])                 - c
# print(text[1])                 - ъ
# print(text[len(text)])         - IndexError (индексация с 0, будет ошибка)
# print(text[len(text)-1])       - к
# print(text[-5])                - б
# print(text[:])                 - print(text)
# print(text[:])                 - съ
# print(text[len(text)-2:])      - ок
# print(text[2:9])               - ешь ещё
# print(text[6:-18])             - еще этих мягких
# print(text[::6])               - сеикакл 
# print(text[0:len(text):6])     - сеикакл    






# ---------------------функция----------------------

# def f(x):
#     if x == 1:
#         return ' целое '
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 2.3 (вернется int 2.3)
# print(f(arg))
# print(type(f(arg)))

# -------------

# def f(x):
#     if x == 1:
#         return ' целое '
#     elif x == 2.3:
#         return 23
#     else:
#         return

# import hello as h
# print(h.f(1))


# -------------

# def new_string(symbol, count):
#     return symbol * count

# print(new_string('!', 5))  #  будет !!!!!
# print(new_string('!'))     #  будет ошибка


# def new_string(symbol, count = 3):
#      return symbol * count

# print(new_string(4))  #  будет умнжение 4 на 3

# -------------

# def concatenatio(*params):
#     res = 0
#     for item in params:
#         res += item
#     return res

# print(concatenatio(1,2,3,4))

# -------------

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', '1'))            # -  a1
# print(concatenatio('a', 's', 'd', 'w'))  # -  asdw