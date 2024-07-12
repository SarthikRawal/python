# 3. Write a Python program to get the smallest number from a list.

def smallest_item(list):
    smallest = list[0]
    for item in list[1:]:
        if item < smallest:
            smallest = item
    return smallest

list = [3, 6, 1, 4, 7]
result = smallest_item(list)
print("Smallest item:", result) 