# 12. Write a Python program to check multiple keys exists in a dictionary.

def multiple_keys_exist(dict, keys):
    return all(key in dict for key in keys)

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    keys = ['a', 'b']
    result = multiple_keys_exist(sample_dict, keys)
    print("Does all keys exists? ", result)
