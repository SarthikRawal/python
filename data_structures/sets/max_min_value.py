# 12. Write a Python program to find maximum and the minimum value in a set.

def max_min_values(set):
    max_value = max(set)
    min_value = min(set)

    return max_value, min_value

if __name__ == '__main__':
    sample_set = {4, 8, 1, 9, 12, 19}

    max, min = max_min_values(sample_set)
    print(f"Max value in set: {max}")
    print(f"Min value in set: {min}")
