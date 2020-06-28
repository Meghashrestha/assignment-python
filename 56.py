# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def listedit(list):
    list1 = []
    for i in range(0, n):
        if (list[i])%2==0:
            element = list[i]
            list1.append(element)
        else:
            pass
    return list1


list=[]
n =int(input("enter the number of item in list: "))
for i in range(0, n):
    element = int(input("enter element"))
    list.append(element)
print(list)
print(listedit(list))