class MathUtils:
    @staticmethod
    def sum(a, b): #Сложение
        return a + b

    @staticmethod
    def difference(a, b): #Вычитание
        return a - b

    @staticmethod
    def multiply(a, b): #Умножение
        return a * b

    @staticmethod
    def divide(a, b): #Деление
        if b == 0:
            raise ValueError("Деление на ноль недопустимо")
        return a / b

    @staticmethod
    def mod(a, b):#Деление по модулю (остаток от деления)
        if b == 0:
            raise ValueError("Деление на ноль недопустимо")
        return a % b

    @staticmethod
    def discriminant(a, b, c): #Вычисление дискриминанта
        return b**2 - 4*a*c