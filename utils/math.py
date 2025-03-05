class MathUtils:

    @staticmethod
    def sum(*args):
        """
        Вычисление суммы произвольного количества чисел.
        """
        result = 0
        for num in args:
            result += num
        return result  # я понимаю, что можно использовать внутреннюю функцию sum и сделать return sum(args), но идея в написании собственной функции

    @staticmethod
    def difference(a, b):
        """ Вычитание """
        return a - b

    @staticmethod
    def multiply(*args):
        """
        Вычисление умножения произвольного количества чисел.
        """
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(a, b):
        """Деление"""
        if b == 0:
            raise ValueError("Деление на ноль недопустимо")
        return a / b

    @staticmethod
    def mod(a, b):
        """Деление по модулю (остаток от деления)"""
        if b == 0:
            raise ValueError("Деление на ноль недопустимо")
        return a % b

    @staticmethod
    def discriminant(a, b, c):
        """Вычисление дискриминанта"""
        return b**2 - 4*a*c