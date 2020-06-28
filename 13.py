#Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).
#Sample Words : red, white, black, red, green, black
#Expected Result : black, green, red, white,red

def string(str):
    str = str.split(",")
    str = sorted(str)
    print(",".join(str))


str=input("enter string seperated by ',' ")
print(string(str))
