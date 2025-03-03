# **Задача 2: Поиск минимального значения**
# У вас есть список чисел. Напишите программу, которая находит минимальное значение в списке через цикл for
#
# Пример данных:
# numbers = [10, 20, 5, 30, 15]
#
# Вывод:
# Минимальное значение: 5

import sys

array_str = sys.argv[1]

array = array_str.split(',')
array = [int(x) for x in array] # Преобразование данных через цикл

print(f"Введенный массив {array}")

min_num = array[0]
for num in array:
    if num < min_num:
        min_num = num

print(f"Минимальное значение: {min_num}")