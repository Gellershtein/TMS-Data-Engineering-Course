import random

a = int (random.randint(10, 99))

first_number = a // 10
second_number = a % 10
sum_letters = first_number + second_number
print(f"Рандомное число {a}, Первая часть {first_number} вторая часть {second_number} сумма чисел {sum_letters}")

reversed_a = second_number*10 + first_number
print(f"Переставленные местами числа {reversed_a}")
