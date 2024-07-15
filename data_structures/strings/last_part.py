# 8. Write a Python program to get the last part of a string before a specified character.

def get_last_part(str, char):
    parts = str.split(char)

    return parts[0]

input_string = "exa mp le. co m/ path"
char = '/'
print(len(input_string.split()))
print(get_last_part(input_string, char))        