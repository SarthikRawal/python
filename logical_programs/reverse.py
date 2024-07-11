# 4. Reverse a number

def reverse_number(num):
    reversed = 0
    while(num > 0):
        remainder = num % 10
        reversed = (reversed*10) + remainder
        num = num//10
    print( reversed)

if __name__ == '__main__':
    number = int(input("Enter a number to reverse: "))
    reverse_number(number)