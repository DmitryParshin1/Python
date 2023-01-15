# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.

# *Пример:* 

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


data = '1, 2, 3, 5, 1, 5, 3, 10'.split()

new_list = []
flag = False

for item in range(len(data)):
    for j in range(item + 1):
        if data[item] == data[j]:
            flag = True
            break
    new_list.append(data[item])
print(new_list)
