'''

26. Write a Python program to insert a given string at the beginning of all items in
a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
'''
def listedit(list):
    for index, value in enumerate(list):
        list[index] = [string + str(list[index])]
        print(list)
    # for i in range(0,n):
    #     element1 = string + str(list[i])
    #     list.append(element1)
    #     new_list = list[n: ]
    # return new_list
list=[]
n=int(input("enter the number of item in list :"))
string=input("enter string: ")
for i in range(0, n):
    element = int(input("enter element"))
    list.append(element)
print(f"first list is ", list)
print(listedit(list))
