# 6. Program to Compute Quotient and Remainder

def quotient_remainder(dividend, divisor):
    if (divisor == 0):
        return "Error: divisor cannot be 0"
    # remainder = dividend % divisor
    # quotient = dividend // divisor
    quotient, remainder = divmod(dividend, divisor)
    return remainder, quotient 

if __name__ == "__main__":
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))

    print(quotient_remainder(dividend, divisor))