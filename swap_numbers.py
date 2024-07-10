# 7. Swap 2 numbers

def swap(a, b):
    a,b = b,a
    return a, b

if __name__ == '__main__':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    
    print(f'before swap: num1 = {num1} & num2 = {num2}')
    num1, num2 = swap(num1, num2)
    print(f'after swap: num1 = {num1} & num2 = {num2}')
