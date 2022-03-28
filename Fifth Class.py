# def slugify(word):
#     return word.replace(" ", "-")

# print(slugify('I am a boy'))

# def slugify(word):
#     return word.replace(" ", "-").lower()

# print(slugify('I am a boy'))



# def first_last(first,last):
#     a = first[:2]
#     b = last[-2:]

#     return a+b 

# print(first_last('Adaobi', 'United'))


# Tim = lambda t : t + 15
# print(Tim(500))

# x = 70
# y = 25
# Tim = lambda x, y : x * y
# print(Tim(x, y))


# numeric = lambda string : string.isnumeric()

# print(numeric("5"))

# J = lambda string : string.swapcase()

# print(J("Timo is A good Boy"))


# step 1: get input from user
# name = input ("File name\n")

# step 2: split and get the last element
# print(name.split("."))

# print(name.split(".")[-1])

# def factorial(n):
#     if n == 1:
#         return 1

#     return n * factorial (n-1)

# print(factorial(1))


# my_list = [2,3,4,5,6]
# trippled = list(map(lambda x : 3*x, my_list))
# print(trippled)

# my_list = [2,3,4,5,6]
# squared = list(map(lambda x : x**2, my_list))
# print(squared)

# a = []
# print(type(a)) 

# b = list[]

# Working with elements in the list
# tim = [2,3,10,5,6,9,8,]
# index =0,1,2,3,4,5,6
# print(tim[5])

# variable = [start:stop:step]
# print(tim[2:5]) 

# tim.sort()
# print(tim)

# tim.reverse()
# print(tim)

# tim.append("3")
# print(tim)

# tim.extend([3,4,5,7,9])
# print(tim)

# tim.insert(5,"inserted")
# print(tim)

# a = [2,3,4,2,[2,3,4,5 [4,52,2],5],24]
# p = a[-1]
# x = a[4][4][1]

# print(p+x)


def largest(arr:list, k:int)
    """ This function returns the highest k values in an array: arr. """

    arr.sort(reverse=True)
    # print(arr)
    return arr[:k]

def smallest(arr:list, k:int)
    """ This function returns the lowest k values in an array: arr. """

    arr.sort()
    return arr[:k]

print(largest([1, 1, 1, 0, 0, 0, 2, -2, -2], 2))






