# 13. Write a Python program to sort a list of tuples using Lambda.

list = [('a', 2), ('b', 3), ('c', 1), ('d', 9), ('e', 4) ]
print(list)
list.sort(key=lambda x: x[1])
print(list)
