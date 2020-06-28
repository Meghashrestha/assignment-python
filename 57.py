# 20. Write a Python program to find intersection of two given arrays using
# Lambda.
def intersection(array1, array2):


    result = list(filter(lambda x: x in array1, array2))
    print(result)


array1 = [1, 2, 3, 4, 5, 6, 7, 8, ]
array2 = [1, 2, 4]
print(array1)
print(array2)
print (intersection(array1, array2))
