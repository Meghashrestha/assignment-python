# 36. Write a Python program to sum all the items in a dictionary.
my_dict = dict()
n= int(input("enter the number of item in the dictionary you want to input : "))
for i in range(0,n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    my_dict[key] = value
print(my_dict)
sum = 0
for keys,value in my_dict.items():
        sum = sum + int(value)
print(f"The sum is ", sum)
