# 6. Write a Python program to remove duplicates from a list.
# 17. Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

# 6.
def remove_duplicate(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

sample_list = [22, 21, 22, 24, 25, 26, 21, 22, 24]
print(remove_duplicate(sample_list))
    
# 17
def remove_dup_list(list):
    seen = set()
    unique_list = []
    for sublist in list:
        # Convert the sublist to a tuple 
        tuple_sublist = tuple(sublist)
        # Check if the tuple is already in the seen set
        if tuple_sublist not in seen:
            # Add the tuple to the seen set and the sublist to the unique list
            seen.add(tuple_sublist)
            unique_list.append(sublist)
    return unique_list

sample = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print(remove_dup_list(sample))