# 4. Harmonic Number

def harmonic_number(n):
    result = 0
    if(n==0):
        return "Enter a valid positive integer number"
    for i in range(1, n + 1):
        result += 1 / i
    return result
num = int(input("Enter the harmonic value: "))

print(harmonic_number(num))