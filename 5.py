#Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. If the
#string length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'
def string(str1):
    length = len(str1)
    str = str1[-3]+str1[-2]+str1[-1]
    if len(str1)>2:
        if str == 'ing':
            str1 = str1 + 'ly'
        else:
             str1 = str1 + 'ing'
    return str1
str1 = input("enter string:")
print(string(str1))
