# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def addition(list):
    sum = 0
    for i in range (0,n):
        sum = sum + list[i]
    return sum


list=[]
n =int(input("enter the number of item in list: "))
for i in range(0, n):
    element = int(input("enter element"))
    list.append(element)
print(list)
print(addition(list))