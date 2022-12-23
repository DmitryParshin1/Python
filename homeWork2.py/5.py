# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# Негафибоначчи

# F(n) = F(n-1) + F(n-2), где n> 1.

number = int(input(' Введите число Фибаначчи: '))

fib = [1,1]
negaFib = [1,-1]

for i in range(2, number):
    my_list = fib[i - 1] + fib[i - 2]
    fib.append(my_list)
    my_list2 = negaFib[i - 2] - negaFib[i - 1]
    negaFib.append(my_list2)

negaFib.reverse()
negaFib.append(0)

print(f' {negaFib + fib}')





# f1 = 1
# f2 = 1
# print(f'{f1}, {f2}', end=', ')

# for i in range(2, number):
#     f1,f2 = f2, f1 + f2
#     print(f2, end=', ')


# f3 = 1
# f4 = 1


# for i in range(-1, number -1):
#     f3,f4 = f4, f3 - f4
#     (print(f4, end=', '))


# print(f4, f2)


