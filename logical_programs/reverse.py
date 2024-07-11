# 4. Reverse a number

def reverse_it(num):
    reversed = 0
    while(num > 0):
        remainder = num % 10
        reversed = (reversed*10) + remainder
        num = num/10
    return reversed

if __name__ == '__main__':
    number = int(input("Enter a number to reverse: "))
    print(reverse_it(number))