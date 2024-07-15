# 8. Write a Python program to remove an item from a tuple.

cities = ('bengaluru', 'mumbai', 'pune', 'delhi')

temp = list(cities)
temp.remove('pune')
tuple(temp)
cities = temp

print(cities)