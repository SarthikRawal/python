# 11. Write a Python program to convert a list into a nested dictionary of keys.

def create_nested_dict(list):
    nested_dict = current = {}
    for key in list:
        current[key] = {}
        current = current[key]
    return nested_dict

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd']
    result = create_nested_dict(sample_list)

    print("Nested Dictionary:", result)