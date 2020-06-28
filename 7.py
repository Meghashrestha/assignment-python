#Write a Python function that takes a list of words and returns the length of the
# longest one.



list1 = []
n = int(input("enter number of words you want to enter:"))
for i in range(0, n):
    element =str(input())
    list1.append(element)
print(list1)
length =len(element)
max = len(list1[0])
temp = list1[0]
for i in list1:
    if len(i) > max:
        max=len(i)
        temp=i
print("The word with the longest length is:")
print(temp)


