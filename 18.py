#18. Write a Python program to get the largest number from a list.
#Write a Python program to sum all the items in a list.
def string(str, n):
    largest = list[0]
    for i in range(0, n):
        if list[i] > largest :
            largest = list[i]
    return largest



list=[]
n=int(input("enter the number of item in list :"))
for i in range(0, n):
    element = int(input("enter element"))
    list.append(element)
print(list)
print(string(str, n))