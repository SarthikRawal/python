# 6. Write a Python program to check whether an element exists within a tuple.

def if_exists(tuple, item):
    for item in tuple:
        if item in tuple:
            return True
        else:
            return False 
        
if __name__ == '__main__':
    my_tuple = (2, 4, 6, 8, 10)
    input = input('Check for element: ')
    print("Element existence:", if_exists(my_tuple, input))