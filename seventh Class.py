# h = 10 
# while h > 0:
#     h-=1

#     print(h)

# h = 1 
# while h <= 10:
#     if h == 10:

#         print("Boom")
#     else:
#         print(h)

#     h+=1

i = 1
while True:

    print(f"keep playing {i}")
    c = input("Continue?\n>")
    if c == "y":
        i+=1
        continue
    else:
        break