# 9. Write a Python program to create a symmetric difference.

def symmetric_diff(set1, set2):
    diff_operator = set1 ^ set2
    
    return diff_operator

if __name__ == '__main__':
    set1 = {'apple', 'banana', 'cherry', 'date'}
    set2 = {'banana', 'date', 'fig', 'grape'}
    
    symmetric_set = symmetric_diff(set1, set2)
    
    print("Set Symmetric difference using the ^ operator:", symmetric_set)