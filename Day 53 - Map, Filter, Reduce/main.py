# # MAP
# # def cube(x):
# #     return x*x*x

# # print(cube(2))

# l = [1,2,3,4,5,6,4,3]
# # newl = []

# # for item in l:
# #     newl.append(cube(item))

# newl = list(map(lambda x: x*x*x, l))

# print(newl)

# #FILTER

# # def filter_Function(a):
# #     return a>4

# newl1 = list(filter(lambda a: a>4, l))

# print(newl1)

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5, 6]

#Calculate the sum of the numbers using the reduce function

sum = reduce(lambda x, y: x + y, numbers)
print(sum)