import sys

for i in range(5):
    if i == 3:
        continue
    print(i)


my_list = list("hello , -98 3")
print(my_list)
mixed_list = [1, "hello", 5.123, [1, 2, 3]]


         # 0  1   2   3    4  ... 100000
         # -5 -4  -3   -2  -1
my_list = [1, 10, 50, 100, 78]

print(my_list[3])
print(my_list[0])
print(my_list[-1], my_list[len(my_list)-1])

   # start stop step
range(0,   5,   1)

# Срезы
print(my_list[1:2:1])
print(my_list[3:4:])
print(my_list[3::])
print(my_list[::2])
print(my_list[3:])
print(my_list[::-1])

my_list[0] = 6
my_list[-1] = 99
my_list[0:2] = [88, 77]
my_list[1:1] = [2, 3]
print(my_list)

text = 'Hello!!'
print(text[2::])
print(text[::-1])

a = 0
b = 2
my_list = [1, 2, 3, 4]
print(my_list[a:b:])

a = [1, 2, 3]
b = a[:] # a.copy()
print(a is b, id(a), id(b))

#     0 1 2
#
# 0   1 2 3
# 1   4 5 6
# 2   8 9 10

matrix = [
    #0  1  2
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9]  # 2
]

print(matrix[1][2])
matrix[1][2] = 999
print(matrix)

summary = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f'i={i} j={j}', matrix[i][j])
        summary += matrix[i][j]
print(summary)


matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

          # 0   1    2    3   4   5
my_list = [999, 345, 123, 78, 31, 123, 345, 123]
my_list = ['dffs', '234dfs', 'asdfds', 'df']
my_list.append(4)
my_list.append(7)
my_list.extend([1,2])
my_list.extend("hello")
my_list.insert(1, 999)
my_list.remove(123)
a = my_list.pop(0)
my_list.clear()
index = my_list.index(76867)
index = my_list.index(123, 3)
cnt = my_list.count(76867)
my_list.sort(key=len, reverse=True)
my_list.reverse()
my_list = my_list + [1,2,3]
my_list = my_list * 3
print(my_list)

my_tuple = tuple()

my_tuple = (1, 2, 3, 5, 123)
my_list = [1, 2, 3, 5, 123]

print(sys.getsizeof(my_tuple))
print(sys.getsizeof(my_list))

my_tuple = (1, 2, 3, 5)
print(my_tuple[1])
print(my_tuple[1:3])

cnt = my_tuple.count(2) # index, sort...
print(cnt)

my_tuple += (3, 4)
print(my_tuple)

# Получаем аргумент командной строки
array_str = "1a2a3"
# Преобразуем строку в список
array = array_str.split('a')

array_new = [int(x) for x in array] # Преобразование данных через цикл

array_new = []
for переменнная in array:
    array_new.append(int(переменнная))
print(array_new)

my_list = [[1, 2], [3, 4], [5, 6]]

for i, j in my_list:
    print(i, j)

my_list = [1, 2, 3]
print(*my_list)
print(1, 2, 3)

my_dict = {
    "name":     ["Alice"],
    "age":      18,
    "country":  "USA",
    42: "Lenina",
    (1, 2, 3): "123",
    "childs":["Alex"],

    "family": {
        "childs": ["Kirill", "Masha"]
    },
}

print(list(my_dict.keys()))
print(list(my_dict.values()))
print(list(my_dict.items()))

for key, value in my_dict.items():
    print(key, ': ', value)



my_dict["name"] = "Masha"
my_dict["name123"] = "Masha2"

my_dict.setdefault("second_name", "Smirnova")
my_dict.update({"name": "Vasuliy", "second_name": "Popov"})

my_dict["name"].append("Vasya")

print(my_dict)


x = {x: x**2 for x in range(5)}
print(x)

del my_dict["name"]
print(id(my_dict))
my_dict.pop("name")
print(id(my_dict))


my_set1 = {1, 2, 3}
my_set2 = {3, 2, 1}

print(my_set1 == my_set2)

my_set = {1, 2, 3}
my_set.add(5)
print(my_set)
my_set.pop()
print(my_set)

my_set.clear()
print(my_set)
#
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
print(set1 | set2)


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.intersection(set2))
print(set1 & set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.difference(set2))
print(set1 - set2)


a = {1, 2, 3}
print(dir(a))


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.symmetric_difference(set2))
print(set1)


set1 = {1, 2, 3}
set2 = {1, 2, 3, 6, 7}

print(set1.issubset(set2))

# frozeset

numbers = [12, 23, 34, 45, 56, 67, 78, 89, 21]

groups = {
    3: [12, 21],
    5: [23]
}