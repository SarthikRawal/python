# 12. Write a Python program to get the difference between the two lists.
# 15. Write a Python program to find common items from two lists.
def difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    new_list = set1 - set2
    return list(new_list)

def common_item(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_list = list(set1 & set2) 
    return common_list

list1 = [2, 6, 8, 10]
list2 = [3, 6, 9, 10]

print("Difference list: ",difference(list1, list2))
print("Common list: ",common_item(list1, list2))