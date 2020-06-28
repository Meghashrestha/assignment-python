# 17. Write a Python program to find if a given string starts with a given character
# using Lambda.
str=input("enter string")
n =input("enter the character to know if the string starts with it or not")
check = lambda x: True if x.startswith(n) else False
print(check(str))

