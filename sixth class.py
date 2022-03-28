# filter
# from curses.ascii import isupper

# x = ['a','b','C','D','e']
# print(list(filter(lambda x:x.isupper(),x)))

# data = input(">").split(',')
# int_data = map(int, data)
# odd_int = filter(lambda x: x%2==1,int_data)
# print(list(odd_int))

# a = "banana"
# b = "banana"

# # print(a==b)

# print(a is b)

# a = [1,2,3]
# b = [1,2,3]
# # print(a==b)
# print(a is b)

# a = [4,7,9]
# b = a 
# c = a.copy()

# # print(b is a)
# print(c is a)

# def middle(arr):
#     return arr[1:-1]

# a = [1,2,3,4,7]
# print(middle(a))

# condition
# name = 15 
# if name==21:
#     print(name)
# else:
#     print(name-2)


# Chained and nested condition

# Chained
# print("What is your exam score?")
# score = int(input(">"))
# if score <= 39:
#     print("f")
# elif score <= 49:
#      print("e")
# elif score <= 59:
#      print("d")


import random
a = (3,2,5,6,8,7)

print(f"Select any number from {a}. We hope it doesn't end in tears")
com_choice = random.choice(a)
random.shuffle(a)
print("Guess the number:")
user_choice = int(input(">>"))

if user_choice in a:
    if user_choice == com_choice:
        print("All power belongs to you comrade")
    else:
        print("Arhhh, comrade. Be like you go try again o.")
else:
    print("Comrade no be so!")  


text = "I am a very good girl"
sub_text = input("Enter text to search for:\n").lower()

lowercase_text = text.lower()
found = lowercase_text.find(sub_text)
count = lowercase_text.count(sub_text)
if found != -1:
    print(f"{count} result(s) found!")
    new_text = text.replace(sub_text,sub_text.upper())
    print(new_text)
else:
    print(f"{count} result(s) found!")


