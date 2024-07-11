# 1. Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.

def print_array(arr):
    for i in range (len(arr)):
        print(arr[i], end=' ')


if __name__ == '__main__':
    arr = [2, 4, 6, 8, 10]
    print_array(arr)
