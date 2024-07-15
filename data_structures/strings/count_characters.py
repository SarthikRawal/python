# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def count_character(str):
    frequency = {}
    for char in str:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

str = "google.com"
result = count_character(str)
print("Character frequency: ", result)

