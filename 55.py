# 9. Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself.

def listedit(n):
    if (n==1):
        return "Not Prime"
    elif (n==2):
        return "Prime"
    else:
        for x in range(2,n):
            if(n % x==0):
                return "Not Prime"
            else:
                return "Prime"
n =int(input("enter the number :  "))

print(listedit(n))