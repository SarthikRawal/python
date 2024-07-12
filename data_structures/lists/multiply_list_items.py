# 2. Write a Python program to multiplies all the items in a list.

def multiply_items(list):
    result = 1
    for i in list:
        result *=i
    return result

sample_list = [12, 2, 4, 5]
result = multiply_items(sample_list)
print("Product of all list items: ", result)
