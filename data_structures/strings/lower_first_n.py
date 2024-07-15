# 12. Write a Python program to lowercase first n characters in a string.

def lower_first_n_char(s, n):
    if n > len(s):
        return "value of n cannot be more then string length"
    return s[:n].lower() + s[n:]

input = "SARTHIK"
print(lower_first_n_char(input, 3))

    