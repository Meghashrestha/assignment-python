# 6. Write a Python function to check whether a number is in a given range.
def inrange(n, x, z):
    if n in range(x,z):
        print("within range")
    else:
        print("not in range")

n = int(input("enter the number you want to check: "))
x = int(input("enter lower limit : "))
z = int(input("enter upper limit :" ))
print(inrange(n, x, z))
