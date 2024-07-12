# 11. Write a Python program to generate all permutations of a list in Python.

# using itertool module
import itertools

def permutations(input_list):
    return list(itertools.permutations(input_list))

# without itertool
def generate_permutations(input_list):
    if len(input_list) == 0:
        return []
    
    if len(input_list) == 1:
        return [input_list]

    perms = []  # List to store permutations
    for i in range(len(input_list)):
        current = input_list[i]
        remaining_list = input_list[:i] + input_list[i+1:]
        for perm in generate_permutations(remaining_list):
            perms.append([current] + perm)

    return perms

input_list = [1, 2, 3]
permutations_list = generate_permutations(input_list)

print("All permutations:")
for perm in permutations_list:
    print(perm)
