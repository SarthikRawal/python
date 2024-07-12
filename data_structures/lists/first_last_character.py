# 4. Write a Python program to count the number of strings where the string length
# is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def count_string(list):
    count = 0
    for item in list:
        if len(item) > 2:
            if item[0] == item[-1]:
                count += 1
    return count

sample = ['abc', 'xyz', 'aba', '1221']
result = count_string(sample)
print(result)