# 19. Write a Python program to create Fibonacci series upto n using Lambda.

from functools import reduce

fibonacci = lambda n: reduce(lambda x, n : x + [x[-1] + x[-2]],
                              range(n - 2), [0, 1])
n = int(input("enter number "))
print(fibonacci(n))