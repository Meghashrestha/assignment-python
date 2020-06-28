# . Write a Python function to find the Max of three numbers.
def max(a, b, c):

    if (a>=b) and (a>=c):
        largest = a
    elif (b>=a) and (b>=c):
        largest = b
    else:
        largest = c
    return largest
list=[]
for i in range(0, 3):
    element = int(input("enter element"))
    list.append(element)
print(list)
a = list[0]
b = list[1]
c = list[2]
print(max(a, b, c))
