# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


number = int(input('Введите число: '))
# number = int(number)
sum = 0

while number > 0:
    a = number % 10
    sum += a
    number //= 10

print(sum)


