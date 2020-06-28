#Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def string(str, function):
    length = len(str)
    place_holder = length/2

    new_str = str[:int(place_holder)] + function + str[int(place_holder):]
    return  new_str


str = input("enter string :")
function = input("enter function :")
print(string(str, function))