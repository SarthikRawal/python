# 6. Write a Python program to create an intersection of sets.

def intersect(set1, set2):
    return set1 & set2

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

result = intersect(x, y)

print("Intersection set:", result)