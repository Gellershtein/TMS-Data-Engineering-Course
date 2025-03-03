import sys
a = sys.argv[0]
b = sys.argv[1]
c = sys.argv[2]

print(a, b, c, sep='\n')

temperature = int(sys.argv[1])
if 20 < temperature < 35:
    print('Погода классная')
elif temperature < -20 or temperature > 35:
    print('Экстремальные условия')

# "in"
fruits = ['apple', 'cherry']
if 'banana' in fruits:
    print('Бананы в списке!')
else:
    print('Бананов нет!')


fruits = "ываловылтьа ывдалвыдла двы аывда вы ш3ук2 ььуь кошка вапваоп ук елкут"
if 'кошка' in fruits:
    print('Буква и есть в строке')
else:
    print('Нет')



# any, all
x = 2
conditions = [x>1, x%2==0, 1==2, True]
if all(conditions):
    print('Все условия выполняются')
else:
    print('Не все условия верны')


# Тернарный оператор
x = 7
if x % 2 == 0:
    result = "Четное"
else:
    result = "Нечетное"
print(result)
result = "Четное" if x % 2 == 0 else "Нечетное"
print(result)


# # is
a = [1, 2, 3]
b = a

print(a, b, sep='\n')

a[0] = 5

print(b, sep='\n')

print(a is b)
c = [1, 2, 3]
print(c is a)

print(id(a), id(b), id(c))
a = "hi"
b = a
c = "hi"
print(a is b)
print(a is c)

a = [1, 2, 3]
b = a.copy()

print(a is b, id(a), id(b))


# Python 3.10 - match

number = -4
match number:
    case 0:
        print("Это ноль")
    case 1:
        print("Это один")
    case 2 | 3 | 5 | 7:
        print("Это простое число")
    case _ if number < 0:
        print("Это отрицательное число")
    case _:
        print("Другое число")

# | - or, или
# & - and, и
# ~ - not, не
# ^ - not or

a = 5 # 101
b = 3 # 011

      # 001 - and
      # 111 - or
result = a & b # 001
print(result)

result = a | b # 111
print(result)

a = 5
print(a << 1) # 1010

set1 = {1, 2, 3}
set2 = {2, 3, 4, 6, 1}
print(set1 & set2)


data = {"name": "Alice", "age": 25}
data = [1, 2]
match data:
    case {"name": name, "age": age}:
        print(f'Имя {name}, Возраст {age}')
    case [x, y, z]:
        print(f"Список из 3 элементов: {x} {y} {z}")
    case _:
        print("ОШИБКА")

a = 1000000
print('Цифра {0:,} по разрядам'.format(a))


# range
            #  start stop step
a = list(range(11,   0,   -1))
print(a)


for i in range(0, 6, 1):
    print(i, i ** 2, sep=' - ')


#     #0  1  2   3
a = [5, 8, 12, 678]
# print("Кол-во: ", len(a))
for i in range(0, len(a)):
    print(f'i - {i}: {a[i]}')

start = 'start'

for letter in "Python":
    print(letter)
    if letter == 'y':
        print('Я ПОЙМАЛ Y')
    a = 1


a = []
while True:
    a.append(100000)
    print(len(a))

# break

for i in range(10):
    print('i - ', i)
else:
    print('Цикл завершен!')

print('Пошел процесс дальше')

for i in range(1, 4):
    for j in range(1, 4):
        print(f'{i} * {j} = {i * j}')
a = []
for i in range(0, 5):
    if i % 2 != 0:
        a.append(i)
print(a)


a = [i for i in range(0, 5) if i % 2 != 0]
print(a)

# kiss - keep it simple stupid

import this
print(this)