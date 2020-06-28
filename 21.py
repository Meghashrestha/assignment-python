#Write a Python program to get a list, sorted in increasing order by the last
#element in each tuple from a given list of non-empty tuples.
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
 #tuple inside list
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


''' 
def element(ele1, ele2):
    list =[]


list = []
n= input("enter the number of set you want to enter : ")
for i in range(0, n):
    element1=int(input())
    element2=int(input())
    list.append(element1,element2)
print(list)
#print(element(ele1,ele2))

'''

