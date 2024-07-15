# 4. Write a Python program to add 'ing' at the end of a given string (length should be at
# least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the

# given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def string_modify(str):
    if len(str) < 3:
        return "string length should be more then 3"
    else: 
        if str[-3:] == 'ing':
            new_str = str+'ly'
        else:
            new_str = str+'ing'
    return new_str


input = input("Enter a string: ")
print(string_modify(input))