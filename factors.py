# 5. Factors

def prime_factors(n):
    factors = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else: 
            i += 1
    if n > 1:
        factors.append(n)
    return factors

number = int(input("Enter a number to get its prime factors: "))
print(prime_factors(number))