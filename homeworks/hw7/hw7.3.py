# **Задача 3: Поиск первого общего элемента в двух списках**
# Условие задачи:
# Даны два списка целых чисел. Необходимо найти первый общий элемент в этих списках и вывести его. Если общего элемента нет, вывести сообщение "Общих элементов нет".
#
# Примеры:
# 1. Входные данные:
# list1 = [3, 7, 8, 12, 15]
# list2 = [5, 7, 9, 12, 18]
#
# Вывод:
# Первый общий элемент: 7
#
# 2. Входные данные:
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# Вывод:
# Общих элементов нет

import sys
import os

# Поднимаемся на два уровня вверх (из 'hw7' → 'homeworks' → 'TMS-Data-Engineering-Course')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.array_check import ArrayCheck

array1 = ArrayCheck.array_input_check(1)
array2 = ArrayCheck.array_input_check(2)
print(f"Первый введенный массив {array1} \nВторой введенный массив {array2}")

#Вариант 1: Решение через массивы
found = False
for num in array1:
    if num in array2:
        print(f"Первый общий элемент: {num}")
        found = True
        break

# Если общих элементов нет
if not found:
    print("Общих элементов нет")

print("-----------------------------------------")

# Вариант 2: Решение через сет (набольших данных будет работать быстрее)
set_array2 = set(array2) #Приведение массива к сету
found = False
for num in array1:
    if num in set_array2:
        print(f"Первый общий элемент: {num}")
        found = True
        break

# Если общих элементов нет
if not found:
    print("Общих элементов нет")