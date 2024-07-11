# 3. Prime Number

def prime_number(num):
    count = 0
    for i in range (1, num+1):
        if (num % i == 0):
            count += 1
    if (count == 2):
        return f"{num} is a prime number"
    else:
        return f"{num} is not a prime number"
    
if __name__ == '__main__':
    number = int(input("Enter a number: "))
    print(prime_number(number))