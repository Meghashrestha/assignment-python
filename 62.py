# 15. Write a Python program to filter a list of integers using Lambda.
list1 = [1, 3, 4, 5, 6, 9, 3]
print(list1)
even = list(filter(lambda x: x%2 == 0, list1))
odd = list(filter(lambda x: x%2 !=0, list1))
print(f"even",even)
print(f"odd", odd)
