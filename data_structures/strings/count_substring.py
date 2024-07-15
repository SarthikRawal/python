# 10. Write a Python program to count occurrences of a substring in a string.

def substring_count(str, substr):
    return str.count(substr)

input_string = "Sarthik"
print(substring_count(input_string, 'ar'))
