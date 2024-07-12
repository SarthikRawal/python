# 11. Write a Python program to use of frozensets.

# Create frozensets from different iterables
fruits_list = ["apple", "banana", "cherry"]
fruits_frozenset = frozenset(fruits_list)

numbers_tuple = (1, 2, 3, 1) 
numbers_frozenset = frozenset(numbers_tuple)

print(fruits_frozenset)  

print("apple" in fruits_frozenset)  

for fruit in fruits_frozenset:
  print(fruit)

modified_fruits = frozenset(fruits_frozenset.union({"kiwi"}))
print(modified_fruits)  

fruit_prices = {"apple": 1.25, "banana": 0.75}
fruit_prices[fruits_frozenset] = 3.00  # Key can be a frozenset here

print(fruit_prices) 
