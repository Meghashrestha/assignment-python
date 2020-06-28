# Write a Python function to create the HTML string with tags around the word(s).
def HTML(str, tag):
    print(f"<%s><%s></%s>"%(tag,str,tag))


str=input("enter string: ")
tag=input("enter tag: ")
print(HTML(str,tag))