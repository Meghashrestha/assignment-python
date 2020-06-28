'''
27. Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
'''

list1 = []
list2 = []
list3 = []
m = int(input("enter the numbeer of item in list 1: "))

for i in range(0, m):
    element = int(input("enter element for list 1"))
    list1.append(element)
n=int(input("enter the number of item in list 2: "))

for i in range(0, n):
    element = int(input("enter element for list 2"))
    list2.append(element)

element = list1[:-1]+list2[:]
list3.append(element)

print("List 1 : ", list1)
print("List 2 : ",list2)
print("the concatinated list is : ", list3)



