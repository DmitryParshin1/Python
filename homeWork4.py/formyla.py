# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc


with open('text.txt', 'w') as data:
    data.write('aaaaabbbcccc')


with open('text.txt', 'r') as data:
    string = data.readline()
data.close

letters = ''
i = 0

while i < len(string):
    value = 0
    while i + 1 < len(string) and string[i] == string[i + 1]:
        value += 1
        i += 1
    letters += str(value) + string[i] + ' '
    i += 1

print(letters)
















# my_dict = {}

# num_list = '3409534095840958204368205879054872958908469181394'

# for dig in num_list:
#     my_dict[dig] = my_dict.get(dig, 0) + 1
# print(my_dict)

# {'3': 4, '4': 7, '0': 7, '9': 8, '5': 6, '8': 8, '2': 3, '6': 2, '7': 2, '1': 2}
               