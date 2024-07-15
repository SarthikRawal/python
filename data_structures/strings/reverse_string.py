# 11. Write a Python program to reverse a string.

def reverse_string(s):
    reversed = ''
    for i in range (len(s)-1, -1, -1):
        reversed += s[i]
    return reversed

input_string = "sarthik"
print(reverse_string(input_string))