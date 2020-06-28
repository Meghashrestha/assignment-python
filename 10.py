#Write a Python program to remove the characters which have odd index values of a given string.
def string(str1):
    n = len(str1)
    final = ''
    for i in range(0,n):
        if i%2 == 0:
            final = final+str1[i]
    return final
str1 = input("enter the string:")
print(string(str1))

''' 
str1 = input("enter the string:")
print(string(str1))
def string(str1):
    n = len(str1)
    for i in range(0,n):
        if i%2 == 0:
            return str1[i]
        else:
            str1[i]=str1[i].replace(str1[i],'')
    return str1

str1 = input("enter the string:")
print(string(str1))
'''