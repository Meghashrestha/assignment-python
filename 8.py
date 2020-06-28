#Write a Python program to remove the nth index character from a nonempty string.

def string(str1):
    char = str1[-1]
    str1=str1.replace(char,'')
    return str1

str1=input("enter the string:")
print("your string is",str1)
print(f"final string is", string(str1))