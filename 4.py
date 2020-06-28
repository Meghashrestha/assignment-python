# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'

def string(str1, str2):
    char1 = str1[0]+str1[1]
    char2 = str2[0]+str2[1]
    str1 = str1.replace(char1, char2)
    str2 = str2.replace(char2, char1)
    return  str1 + ' '+ str2

str1=input("enter str1:")
str2= input("enter str2:")
print(string(str1, str2))