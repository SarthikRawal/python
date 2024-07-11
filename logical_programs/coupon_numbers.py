# 5. Generate coupon number
import random

def coupon_number(num):
    coupons = set()
    random_numbers = 0
    while len(coupons) < num:
        coupon = random.randint(1, num)
        coupons.add(coupon)
        random_numbers += 1
    return random_numbers

if __name__ == '__main__':
    random_number = int(input("Enter a number to generate random coupon: "))
    result = coupon_number(random_number)
    print(f"total random number needed to have all distinct numbers is {result}")