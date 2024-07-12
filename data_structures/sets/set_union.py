# 7. Write a Python program to create a union of sets.


def union(set1, set2):
    return set1 | set2

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

result = union(x, y)

print("Union set:", result)