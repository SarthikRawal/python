# 13. Write a Python program to count number of items in a dictionary value that is a list.

def count_items(dict):
    count = 0
    for value in dict.values():
        if isinstance(value, list):
            count += len(value)
    return count

if __name__ == '__main__':
    sample_dict = {
        'fruits': ['apple', 'banana', 'cherry'],
        'vegetables': ['carrot', 'broccoli'],
        'drinks': 'water',
        'snacks': ['chips', 'nuts']
    }
    result = count_items(sample_dict)
    print("Total Number of items: ", result)