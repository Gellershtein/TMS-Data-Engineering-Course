class MathUtils:
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def difference(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Деление на ноль недопустимо")
        return a / b

    @staticmethod
    def mod(a, b):
        if b == 0:
            raise ValueError("Деление на ноль недопустимо")
        return a % b