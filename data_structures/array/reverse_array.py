# 2. Write a Python program to reverse the order of the items in the array.

def reverse_array(arr):
    rev_arr = []
    for i in range(len(arr)-1, -1, -1):
        rev_arr.append(arr[i])
    return rev_arr

if __name__ == '__main__':
    arr = [2, 4, 6, 8, 10]
    print("original array: ", arr)
    rev_array = reverse_array(arr)
    print("reversed array: ", rev_array)