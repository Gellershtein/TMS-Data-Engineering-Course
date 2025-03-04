# **Задача 1: Классификация данных**
# - У вас есть список чисел. Напишите программу, которая классифицирует числа на:
# "Маленькое" (меньше 10),
# "Среднее" (от 10 до 50),
# "Большое" (больше 50).
# - ввод массива реализовать через параметры - sys
#
# Пример данных:
# numbers = [5, 15, 60, 3, 45, 70]
#
# Вывод:
# 5 — Маленькое
# 15 — Среднее
# 60 — Большое
# 3 — Маленькое
# 45 — Среднее
# 70 — Большое
#
#
# Подсказка:
# Чтобы ввести массив данных как параметр, можно использовать:
# # Получаем аргумент командной строки
# array_str = sys.argv[1]
# # Преобразуем строку в список
# array = array_str.split(',')
# array = [int(x) for x in array] # Преобразование данных через цикл

import sys
import os

# Поднимаемся на два уровня вверх (из 'hw7' → 'homeworks' → 'TMS-Data-Engineering-Course')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.array_check import ArrayCheck

array = ArrayCheck.array_input_check(1)
print(f"Введенный массив {array}")

# Вариант 1. Через match
for num in array:
    f_data = f"{num}"
    match num:
        case _ if num < 10:
            print(f_data + " - Маленькое")
        case _ if 10 <= num <= 50:
            print(f_data + " - Среднее")
        case _ if num > 50:
            print(f_data + " - Большое")

print("-----------------------------------------")

# Вариант 2. Упрощенный вариант через тернарный оператор
for num in array:
    classification = (
        "Маленькое" if num < 10 else
        "Среднее" if 10 <= num <= 50 else
        "Большое"
    )
    print(f"{num} — {classification}")
