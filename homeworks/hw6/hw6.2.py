import random
from utils.math import MathUtils
# **Задача 2: Вычисление суммы и произведения цифр числа**
# Напишите программу, которая:
# - Запрашивает у пользователя трёхзначное число (тип int).
# - Вычисляет сумму и произведение его цифр.
# - Выводит результат.


while True:
    try:
        three_digit_number = int(input("Введите трёхзначное число: "))
        if three_digit_number > 999 or three_digit_number < 100:
            print(f"Нужно ввести трёхзначное число введенное число: {three_digit_number}")
            continue
        else:
            print(f"Введенное трёхзначное число: {three_digit_number}")
            break
    except ValueError:
        print("Введите трёхзначное число")

# #Рандомная генерация чисел для задачи
#
# three_digit_number = int (random.randint(100, 999))
# print(f"Введенное трёхзначное число: {three_digit_number}")
# print(f"Вычисляем числа по разрядам в числе {three_digit_number}")

first_digit_number = three_digit_number//100
two_digit_number = (three_digit_number%100)
second_digit_number = two_digit_number//10
third_digit_number = two_digit_number%10
print(f"Введенное трёхзначное число: {three_digit_number}, первый разряд = {first_digit_number} второй разряд = {second_digit_number}  трейтий разряд = {third_digit_number}")
three_digit_numbers_sum = MathUtils.sum(MathUtils.sum(first_digit_number, second_digit_number), third_digit_number)
three_digit_numbers_multipling = MathUtils.multiply(MathUtils.multiply(first_digit_number, second_digit_number), third_digit_number)
print(f"Вычисляем сумму и произведение цифр трёхзначного числа {three_digit_number}, Сумма чисел = {three_digit_numbers_sum}, Произведение чисел = {three_digit_numbers_multipling}")