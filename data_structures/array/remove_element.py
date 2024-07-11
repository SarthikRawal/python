# 4. Write a Python program to remove the first occurrence of a specified element from an array.

def remove_first_occurrence(ele, arr):
    for i in range (len(arr)):
        if arr[i] == ele:
            arr.remove(arr[i])
            return arr
    return "element not present"

if __name__ == '__main__':
    arr = [2, 4, 5, 1, 4, 9]
    element = 4
    print(remove_first_occurrence(element, arr))
