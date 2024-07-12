# 8. Write a Python program to create set difference.

def set_difference(set1, set2):
    diff_operator = set1 - set2
    
    return diff_operator

if __name__ == '__main__':
    set1 = {'apple', 'banana', 'cherry', 'date'}
    set2 = {'banana', 'date', 'fig', 'grape'}
    
    diff_operator = set_difference(set1, set2)
    
    print("Set difference using the - operator:", diff_operator)