# 6. Write a Python program to remove a key from a dictionary.

def remove_key(dict, key):
    if key in dict:
        del dict[key]
        return dict
    else:
        return f"Key {key} not found"
    
if __name__ == '__main__':
    fruits = {
        "apple": 10,
        "mango": 9,
        "orange": 16,
        "lemon": 8,
    }
    print(remove_key(fruits, "lemon"))