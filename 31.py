# 31. Write a Python program to iterate over dictionaries using for loops.
my_dict = dict()
n= int(input("enter the number of item in the dictionary you want to input : "))
for i in range(0,n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    my_dict[key] = value
print(my_dict)
for key, value in my_dict.items():
    print(key,'dictionary item is',my_dict[key])
