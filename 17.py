#17. Write a Python program to multiplies all the items in a list.
#Write a Python program to sum all the items in a list.
def string(str, n):
    multiply = 1
    for i in range(0, n):
        multiply = multiply * list[i]
    return multiply



list=[]
n=int(input("enter the number of item in list :"))
for i in range(0, n):
    element = int(input("enter element"))
    list.append(element)
print(list)
print(string(str, n))