# 3. Напишите программу, которая определит 
# позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# my_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# my_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
my_list = ["123", "234", 123, "567"]
# my_list = []

print(my_list)
flag = -1
index = 0

a = input( ' Введите искомую строку: ')

for iten in range(len(my_list)):
    if a == my_list[iten]:
        flag += 1
        if flag == 1:
            index = iten
            break
if flag == 1:
    print(f'Второе вхождение строки {a} - {index}')
else:
    print(f'НЕТ второго вхождения строки {a}')

