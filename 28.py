'''
Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''

dict={0:1}
dict1={}

print(dict)

n=int(input("do you want to add a key to the dictionary? 1 for yes ,0 for no : "))
if n==1:
    keys = input("keys")
    value = input("value ")
    dict1={keys:value}
    dict.update(dict1)

else:
    pass
print(dict)


