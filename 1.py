#1. Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com'

def string(str1):
    dict = {} #dict = {"key : value"}
    for n in str1 :
         keys = dict.keys()
         if n in keys:
             dict[n] += 1
         else:
             dict[n] = 1
    return dict
print(string('google.com'))

