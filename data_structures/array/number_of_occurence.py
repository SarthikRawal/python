# 3. Write a Python program to get the number of occurrences of a specified element in an array.

def number_of_occurrence(ele, arr):
    count = 0
    for i in range (len(arr)):
        if arr[i] == ele:
            count += 1
    return count

if __name__ == '__main__':
    arr = [2, 5, 2, 6, 7, 5, 6]
    element = 2
    result = number_of_occurrence(element, arr)
    print(f"{result} number of times '{element}' occured in the array.")