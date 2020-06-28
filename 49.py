# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def addition(list):
    mul = 1
    for i in range (0,n):
        mul = mul * list[i]
    return mul


list=[]
n =int(input("enter the number of item in list: "))
for i in range(0, n):
    element = int(input("enter element"))
    list.append(element)
print(list)
print(addition(list))