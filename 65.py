# 18. Write a Python program to check whether a given string is number or not
# using Lambda.
str = input("enter string: ")
check = lambda x: True if str.isdigit() else False
print(check(str))

