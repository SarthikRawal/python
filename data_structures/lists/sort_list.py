# 5. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def sort_by_last_element(list):
    return sorted(list, key = lambda x: x[-1])


sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = sort_by_last_element(sample_list)
print("Sorted by last element:", result)