#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the
#empty string.
def string(str1):

     if len(str1)>1:
         print(str1[0]+str1[1]+str1[-2]+str1[-1])
     else:
         print("empty string")
print(string("python"))
str1 = input("Enter a string:")
print(string(str1))
