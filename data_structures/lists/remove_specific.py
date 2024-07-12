# 10. Write a Python program to print a specified list after removing the 0th, 4th and
# 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def remove_specific(list):
    list.pop(5)
    list.pop(4)
    list.pop(0)
    return list

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("after removing 0th, 4th & 5th item: ",remove_specific(sample_list))