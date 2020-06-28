# 14. Write a Python program to sort a list of dictionaries using Lambda.
list = [{"a": 2, "rank": 7}, {"b": 3, "rank": 2}, {"c": 1, "rank": 3}, {"d": 9, "rank": 9}, {"e": 4, "rank": 1} ]
print(list)
list = sorted(list, key = lambda x: x['rank'])
print(list)