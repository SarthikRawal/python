# 10. Write a Python program to reverse a tuple.

def reverse_tuple(my_tuple):
    reversed_list = []
    for i in range(len(my_tuple) - 1, -1, -1):
        reversed_list.append(my_tuple[i])
    reversed_tuple = tuple(reversed_list)
    return reversed_tuple

cities = ('bengaluru', 'mumbai', 'pune', 'delhi')

reversed_tuple = reverse_tuple(cities)
print(reversed_tuple)