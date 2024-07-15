# 3. Write a Python program to get a string from a given string where all occurrences of its
# first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

def replace_char(str):
    first_char = str[0]
    new_str = first_char + str[1:].replace(first_char, '$')
    return new_str

sample = 'restart'
print(replace_char(sample))