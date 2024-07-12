# 8. Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string.

def dict_from_string(str):
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

if __name__ == '__main__':
    string = "w3resource"
    result_dict = dict_from_string(string)
    print("New Dictionary: ", result_dict)