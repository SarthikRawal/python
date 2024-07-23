# Python comprehensions (List, Dictionary and Set)

# List
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of squares of even numbers from 0 to 9
squares = [x*x for x in num if x%2 == 0]
# print(squares)

# pair each letter in 'abcd' and each number in '0123'
my_list = [(letter, num) for letter in 'abcd' for num in range(4) ]
print (my_list)

# list without vowel
words = ["sky", "fly", "try", "apple", "banana"]
without_vowel = [word for word in words if all(v not in word for v in "aeiou")]
print(without_vowel)

# Dictionary

# square number
my_sq_dict = {x: x*x for x in range(1, 11)}
print(my_sq_dict)

# character frequency
string = 'comprehensions'
char_dict = {char: string.count(char) for char in string}
print(char_dict)

# inverts items
my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

new_dict = {val: key for key, val in my_dict.items()}
print(new_dict)

# filter dictionary
prices = {'apple': 5, 'banana': 12, 'cherry': 20, 'date': 3}
filter_dict = {item: price for item, price in prices.items() if price > 10}
print(filter_dict)

# Generator Function

# def gen_func(num):
#     for n in num:
#         yield n*n

my_gen = (n*n for n in num)

for i in my_gen:
    print (i)
print(type(my_gen))