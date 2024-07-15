# 5. Write a Python program to find the repeated items of a tuple.

def repeated_items(tup):
    repeated = []
    for item in tup:
        if tup.count(item) > 1 and item not in repeated:
            repeated.append(item)
    return repeated

if __name__ == '__main__':
    my_tuple = (1, 2, 3, 3, 4, 5, 5, 1)
    print('Repeated items:', repeated_items(my_tuple))