# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
def string(str1):

    snot = str1.find('not')
    spoor = str1.find('poor')
    if spoor > snot:
       str1= str1.replace(str1[snot : spoor], '')
    else:
        return "the sentence is not valid for  program"

    return str1
print(string("The lyrics is not that poor!"))
str1 = input("enter a sentence which includes 'not' and 'poor'.")
print(string(str1))