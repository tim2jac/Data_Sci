# a = "Ada is a boy"
# print(a.split())
# print(a.split(","))
# print(a.split("."))



# a = ['A', 'quick', 'brown', 'fox', 'just', 'died.']

# b = "".join(a)

# print(b.replace("brown", "white"))

# a = ['A', 'quick', 'brown', 'fox', 'just', 'died.']

# b = " ".join(a)

# print(b.replace("brown", "white"))


# arr = [1,2,3,4,5,6]

# mapped = map(lambda y : y**2, arr)

# print(sum(mapped))

# arr = [1,2,3,4,5,6]

# mapped = map(lambda y : y**2, arr)

# print(min(mapped))

# arr = [1,2,3,4,5,6]

# mapped = map(lambda y : y**2, arr)

# print(max(mapped))

# arr = [1,2,3,4,5,6]

# mapped = map(lambda y : y**2, arr)

# print(list(mapped))

# arr = [1,2,3,4,5]
# print(sum(arr)/len(arr))

# arr = [1,2,3,4,5]
# print(max(arr)-(min(arr))

# t = "2,3,4,7,8"
# print(t.split(','))


# r = input("write a number")

# arr = r.split(",")
# print(arr)
# print(list(map(int, arr)))

# xmean = map(lambda x: (x-mean))

# from math import sqrt
# from statistics import variance

# tj_score = input("enter student score")
# tj_split = tj_score.split(',')
# print(tj_split)
# tj_list = list(map(int,tj_split))
# print(tj_list)
# average = sum(tj_list)/len(tj_list)
# print(average)
# range = max(tj_list) - min(tj_list)
# print(range)

# xmean = map(lambda x: (x-average)**2,tj_list)
# std = sqrt(sum(xmean)/len(tj_list))
# variance = std**2

# print(f"Mean: {average}")
# print(f"Range: {range}")
# print(f"Standard Deviation: {std}")
# print(f"Variance: {variance}")


# age = int(input("Age:\n"))
# print(f"you were born in {2022-age}")

# def add_num(a,b):
#     print(a+b)
# x = add_num(4,6)
# print(x)

# def add_num(a,b):
#     print(a+b)
#     return a+b
# x = add_num(4,6)
# print(x)

# def add_num(a,b):
#     return a+b
#     print(a+b)
# x = add_num(4,6)
# print(x)


# def factorial(n):
#     if n == 1:
#         return 1

#     return n * factorial (n-1)

# print(factorial(1))

# def factorial(n):
#     if n == 1:
#         return 1

#     return n * factorial (n-1)

# print(factorial(5))


import re


def miles__to_kilo(miles):
    return miles*1.6

print(miles__to_kilo(50))

def dollar_to_naira(dollar):
    return dollar*599

print(dollar_to_naira(2000))

