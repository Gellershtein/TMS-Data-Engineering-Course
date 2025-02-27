import random
# **Задача 3. Доступ в систему**
# Условие:
# Пользователь может получить доступ к системе, если:
# Он ввёл правильный логин И правильный пароль
# ИЛИ У него есть специальный токен доступа
#
# Что должна сделать программа:
# - Запрашивает у пользователя 3 значения (необходимо определить самостоятельно по заданному условию, тип bool) пример:
# login_correct = ….(input("Правильный логин? (True/False): "))
# (вместо точек нужно сделать приведение типа)
# - Вывести, есть ли у пользователя доступ по введенным значениям

# is_Login_Correct = bool(int(input("Введите значение is_Login_Correct (1 - True, 0 - False): ")))
# is_Password_Correct = bool(int(input("Введите значение is_Password_Correct (1 - True, 0 - False): ")))
# is_Admin = bool(int(input("Введите значение is_Admin (1 - True, 0 - False): ")))
#
# print(f"Введенные значения: is_Login_Correct = {is_Login_Correct}, is_Password_Correct = {is_Password_Correct}, is_Admin = {is_Admin}")

# #Рандомная генерация чисел для задачи
is_Login_Correct, is_Password_Correct, is_Admin = random.choice([True, False]), random.choice([True, False]), random.choice([True, False])
print(f"Введенные значения: is_Login_Correct = {is_Login_Correct}, is_Password_Correct = {is_Password_Correct}, is_Admin = {is_Admin}")

if is_Admin:
    # Если пользователь является администратором, доступ разрешен
    print(f"Доступ разрешен: Пользователь является администратором.(is_Admin = {is_Admin})")
elif is_Login_Correct and is_Password_Correct:
    # Если логин и пароль верны, доступ разрешен
    print(f"Доступ разрешен: Логин и пароль верны.(is_Login_Correct = {is_Login_Correct}, is_Password_Correct = {is_Password_Correct})")
else:
    # Во всех остальных случаях доступ запрещен
    print(f"Доступ запрещен: Неверный логин или пароль, и пользователь не является администратором. (is_Login_Correct = {is_Login_Correct}, is_Password_Correct = {is_Password_Correct}, is_Admin = {is_Admin})")