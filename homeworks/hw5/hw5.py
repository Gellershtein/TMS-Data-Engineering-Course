from utils.math import MathUtils

print("\nД/з по теме Урок 5: Введение в Python: Основы синтаксиса\n")
print("----------Легкий уровень----------")

print("\n1. Сложение чисел: Посчитайте и выведите сумму чисел 7 и 15.")
print("Сумма чисел 7 и 15 =", MathUtils.sum(7, 15))

print("\n2. Арифметические операции: Вычислите разность чисел 25 и 10 и выведите результат.")
print("Разность чисел 25 и 10 =", MathUtils.difference(25, 10))

print("\n3. Умножение: Найдите произведение чисел 6 и 8 и выведите результат.")
print("Произведение чисел 6 и 8 =", MathUtils.multiply(6, 8))

print("\n4. Деление: Поделите число 20 на 4 и выведите результат.")
print("Деление чисел 20 на 4 =", MathUtils.divide(20, 4))

print("\n5. Комбинация операций: Вычислите результат выражения (10 + 5) * 2 и выведите его.")
result = MathUtils.multiply(MathUtils.sum(10, 5), 2)
print("Результат выражения (10 + 5) * 2 =", result)

print("\n----------Средний уровень----------")

print("\n6. Остаток от деления: Найдите остаток от деления числа 17 на 3 и выведите результат.")
print("Остаток от деления числа 17 на 3 =", MathUtils.mod(17, 3))

print("\n7. Выражение с несколькими операциями: Вычислите значение выражения (15 - 3) * (2 + 4) / 6 и выведите результат.")
result = MathUtils.divide(
    MathUtils.multiply(
        MathUtils.difference(15, 3),
        MathUtils.sum(2, 4)
    ),
    6
)
print("Значение выражения (15 - 3) * (2 + 4) / 6 =", result)

print("\n8. Работа с дробями: Поделите число 22 на 7 и выведите результат как десятичное число.")
result = MathUtils.divide(22, 7)
print("Результат деления 22 на 7 =", result)

print("\n----------Продвинутый уровень----------")

print("\n9. Сложное выражение: Вычислите результат выражения (10 + 20) / 5 + 3 * (8 - 2) и выведите результат.")
result = MathUtils.sum(
    MathUtils.divide(MathUtils.sum(10, 20), 5),
    MathUtils.multiply(3, MathUtils.difference(8, 2))
)
print("Результат выражения (10 + 20) / 5 + 3 * (8 - 2) =", result)

print("\n10. Операции со скобками: Посчитайте значение выражения 100 - (30 / (2 + 3)) * 4 + 10 и выведите его.")
result = MathUtils.sum(
    MathUtils.difference(
        100,
        MathUtils.multiply(
            MathUtils.divide(30, MathUtils.sum(2, 3)),
            4
        )
    ),
    10
)
print("Результат выражения 100 - (30 / (2 + 3)) * 4 + 10 =", result)