#Write a Python program to check a list is empty or not.

def string(list):
    length = len(list)
    if length == 0 & n==0:
        print("list is empty")
    else:
        print("list is not empty")



list=[]
n=int(input("enter the number of item in list :"))
for i in range(0, n):
    element = int(input("enter element"))
    list.append(element)
print(list)
print(string(list))
