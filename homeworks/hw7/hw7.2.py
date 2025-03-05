# **Задача 2: Поиск минимального значения**
# У вас есть список чисел. Напишите программу, которая находит минимальное значение в списке через цикл for
#
# Пример данных:
# numbers = [10, 20, 5, 30, 15]
#
# Вывод:
# Минимальное значение: 5

import sys
import os

# Поднимаемся на два уровня вверх (из 'hw7' → 'homeworks' → 'TMS-Data-Engineering-Course')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.array_check import ArrayCheck

array = ArrayCheck.array_input_check(1)
print(f"Введенный массив {array}")

min_num = array[0]
for num in array:
    if num < min_num:
        min_num = num

print(f"Минимальное значение: {min_num}")