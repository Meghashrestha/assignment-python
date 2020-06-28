# 43. Write a Python program to remove an item from a tuple.
tup = (1, 2, 3, 4, 5)
print(tup)
tupl = list(tup)
element = int(input("enter key of an item you want to remove "))
tupl.pop(element)
tup = tuple(tupl)
print(tup)
