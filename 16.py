#Write a Python program to sum all the items in a list.
def string(str, n):
    sum = 0
    for i in range(0, n):
        sum = sum + list[i]
    return sum



list=[]
n=int(input("enter the number of item in list :"))
for i in range(0, n):
    element = int(input("enter element"))
    list.append(element)
print(list)
print(string(str, n))