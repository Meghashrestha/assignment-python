 #Write a Python program to count the occurrences of each word in a given sentence.
def string(str1):
    dict={}
    words = str1.split()
    for n in words:
         if n in dict:
            dict[n] += 1
         else:
            dict[n] = 1
    return dict
str1=input("enter the sentence:")
print(string(str1))
