# 8. Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def listedit(list):
    list1 = []
    for i in range(0,n):
        if i not in list1:
            element = list[i]
            list1.append(element)
    print(list1)

list=[]
n =int(input("enter the number of item in list: "))
for i in range(0, n):
    element = int(input("enter element"))
    list.append(element)
print(list)
print(listedit(list))