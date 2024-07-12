# 9. Write a Python function that takes two lists and returns True if they have at least one common member

def find_common(list1, list2):
    commom = False
    for i1 in list1:
        for i2 in list2:
            if i1 == i2:
                commom = True
    return commom

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 6, 7, 8, 9]
    print(find_common(list1, list2))