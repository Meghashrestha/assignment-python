# 40. Write a Python program to add an item in a tuple.
tup = ()
n=int(input("enter number of item you want to add in tuple : "))
for i in range(0, n):
    element = input("enter item: ")
    tup = tup + (element,)
    print(tup)