# 3. Power of 2

def power_of_2(n):
    if(0<= n <31):
        for i in range (n+1):
            print (f'2^{i} = {2**i}')
    else:
        return "enter value b/w 0-31"
power = int(input("Enter the power value: "))

print(power_of_2(power))