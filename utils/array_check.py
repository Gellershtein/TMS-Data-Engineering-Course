import sys

class ArrayCheck:

    @staticmethod
    def array_input_check(index):
        """ Метод проверки введенного массива из аргументов """
        try:
            array_str = sys.argv[index]  # Берем аргумент по индексу
        except IndexError:
            print(f"Ошибка: Массив пустой.")
            sys.exit(1)

        try:
            array = [int(x.strip()) for x in array_str.split(',')]
        except ValueError:
            print(f"Ошибка: Введенные данные должны быть числами, разделенными запятыми.")
            sys.exit(1)
        return array