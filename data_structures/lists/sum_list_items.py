# 1. Write a Python program to sum all the items in a list.

def sum_item(list):
    sum = 0
    for item in list:
        sum += item
    return sum

if __name__ == '__main__':
    sample_list = [2, 6, 8, 10, 14]

    result = sum_item(sample_list)
    print(f"Sum of all list items:", result)