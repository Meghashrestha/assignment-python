#20. Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character are same from a given list of
#strings.

def string(str):
    list=[]
    sum = 0
    list = str.split(" ")
    n = len(list)
    for n in list:
        if n > 2:
            sum = sum + list.index(i)
            print(sum)
        else:
            return "wrong"
    return sum



str = input("enter a string : ")
print(string(str))