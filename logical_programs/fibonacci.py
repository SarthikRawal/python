# 1. Fibonacci series

def fibonacci(n):
    if n <= 1:
       return n
    else:
       return(fibonacci(n-1) + fibonacci(n-2))

if __name__ == '__main__':
    num = int(input("enter te range: "))
    for i in range (num):
        print(fibonacci(i), end=', ')