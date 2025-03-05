#Task 1
# matrix_a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# matrix_b = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]
#
# for i in range(len(matrix_a)):
#     for j in range(len(matrix_a[0])):
#         matrix_a[i][j] = matrix_a[i][j] + matrix_b[i][j]
# print( matrix_a)

# my_tuple = tuple()
# my_tuple = (1,2,3)
# print(my_tuple)

#Task 2
# numbers = [12, 23, 34, 45, 56, 67, 78, 89, 21, 30]
# groups = {}
#
# for num in numbers:
#     sum_digits = sum(int(x) for x in str(num))
#     if sum_digits in groups.keys():
#         groups[sum_digits].append(num)
#     else:
#         groups[sum_digits] = [num]
#
# print(groups)