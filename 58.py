# 11. Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.


x= int(input("enter x "))
y = int(input("enter y "))
result1 = lambda x : x + 15
result2 = lambda x, y : x*y
print(result1(x))
print(result2(x, y))