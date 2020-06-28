#24. Write a Python program to clone or copy a list.

def copylist(list2):
    list2=[]
    list2=list.copy()
    return list2


list=[]
list2=[]
n=int(input("enter the number of item in list :"))
for i in range(0, n):
    element = int(input("enter element"))
    list.append(element)
print(f"list 1 is ",list)
print(f"copied list is ", copylist(list2))
