# 7. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def checkcase(str):
    d = {"uppercase": 0, "lowercase": 0}
    for i in str:
        if i.isupper():
            d["uppercase"] +=1
        elif i.islower():
            d["lowercase"] +=1
        else:
            pass
    print(f"the number of upper cases is ", d["uppercase"])
    print(f"the number of lowercase cases is ", d["lowercase"])


str = input(" enter string : ")
print(checkcase(str))


