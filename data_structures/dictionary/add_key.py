# 2. Write a Python script to add a key to a dictionary.

fruits = {
    "apple": 10,
    "mango": 9,
    "orange": 16,
    "lemon": 8,
}
if __name__ == '__main__':
    # adding indivdually
    fruits["kiwi"] = 8
    print("-->", fruits)
    
    # adding muiltiple at once
    new_fruits = {
        "banana": 12,
        "grapes": 7
    } 
    fruits.update(new_fruits)
    print("-->", fruits)