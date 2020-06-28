#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
def string(str1):
    char1 = str1[0]
    char2 = str1[-1]
    temp = char1
    char1 = char2
    char2 = temp
    return char1 + str1[1:-1] + char2


str1=input("enter string")
print(string(str1))