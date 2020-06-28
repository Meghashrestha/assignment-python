#19. Write a Python program to get the smallest number from a list.
#18. Write a Python program to get the largest number from a list.
#Write a Python program to sum all the items in a list.
def string(str, n):
    smallest = list[0]
    for i in range(0, n):
        if list[i] < smallest :
            smallest = list[i]
    return smallest



list=[]
n=int(input("enter the number of item in list :"))
for i in range(0, n):
    element = int(input("enter element"))
    list.append(element)
print(list)
print(string(str, n))