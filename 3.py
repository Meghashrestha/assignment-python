#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'


def string(str1):
    str0 = str1[0]
    str1 = str1.replace(str0,'$')
    str1 = str0 + str1[1:]
    print(str1)
    return str1

str1 = input("enter string:")
print(string(str1))
