# 2. Perfect number

def perfect_number(num):
    if (num <= 0):
        return "Enter a positive integer number"
    n = 0
    for i in range (1, num):
        if (num % i) == 0:
            n += i
    if(n == num):
        return f"{num} is a perfect number"
    else:
        return f"{num} is not a perfect number"
             

number = int(input("Enter a number: "))
print(perfect_number(number))