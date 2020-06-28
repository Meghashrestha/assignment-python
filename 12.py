# Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.
def string(str1):
    print(f"original string",str1)
    print(f"String uppercase:",str1.upper())
    print(f"String lowercase",str1.lower())



str1=input("enter a string : ")
print(string(str1))
