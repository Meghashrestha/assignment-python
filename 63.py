# 16. Write a Python program to square and cube every number in a given list of
# integers using Lambda.
list1 = [1, 3, 4, 5, 6, 9, 3]
print(list1)
square = list(map(lambda x: x**2, list1))
cube = list(map(lambda x: x**3, list1))
print(f"square",square)
print(f"cube", cube)
