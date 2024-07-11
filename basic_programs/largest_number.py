# 10. Largest among three numbers

def largest_number(a, b, c):
    if b < a > c:
        return f"{a} is largest"
    elif a < b > c:
        return f"{b} is largest"
    else: 
        return f"{c} is largest"

if __name__ == '__main__':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    print(largest_number(num1, num2, num3))