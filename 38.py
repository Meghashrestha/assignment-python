# 38. Write a Python program to remove a key from a dictionary.
my_dict = dict()
n= int(input("enter the number of item in the dictionary you want to input : "))
for i in range(0,n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    my_dict[key] = value
print(my_dict)
m = input("enter the key of an item you want to remove : ")
if m in my_dict:
    my_dict.pop(m)
print(my_dict)