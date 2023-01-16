# Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension


# list comprehension  -----------------------


# from random import randint as RI

# my_list = [RI(0,10) for x in range(10) if x%2 !=0]

# print(my_list)



# map  -----------------------



# my_list = [x for x in range(10)]

# # print(my_list)

# # for i in range(len(my_list)):
# #     my_list[i] = str(my_list[i])     # переводим в строки

# my_list = list(map(str, my_list))

# print(my_list)



# filter  -----------------------



# my_list = '234 564 566 345 324 876 452 789'
# print(my_list)


# # my_list = list(filter(lambda x: not '4' in x, my_list.split()))

# # print(my_list)

# my_list = list(filter(lambda x: x%2 ==0, list(map(int,my_list.split()))))

# print(my_list)



# enumerate  -----------------------



# my_list = '234 564 566 345 324 876 452 789'
# my_list = my_list.split()
# print(my_list)

# # for i in my_list:
# #     print(i)

# # for i in range(len(my_list)):
# #     print(my_list[i])

# for i in range(len(my_list)):
#     print(i + 1, my_list[i])

# print('------------------')

# for i, item in enumerate(my_list, 1):
#     print(i, item)




# zip  -----------------------


# my_list = '234 564 566 345 324 876 452 789'.split()
# my_list2 = [1, 56, 43, 678, 543, 56, 78, 43]

# print(list(zip(my_list, my_list2)))




# lambda  -----------------------


