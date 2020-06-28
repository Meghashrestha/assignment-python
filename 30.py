#  Write a Python script to check whether a given key already exists in a
# dictionary.

my_dict = dict()
n= int(input("enter the number of item in the dictionary you want to input : "))
for i in range(0,n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    my_dict[key] = value
print(my_dict)
m=input("enter a key to check: ")
if m in my_dict:
    print("yes")
else:
    print("no")

