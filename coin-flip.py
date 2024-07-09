# 1. Flip Coin and print percentage of Heads and Tails
import random

def coin_flip(num_of_flips):
    heads = 0
    tails = 0
    for i in range(num_of_flips):
        coin_toss = random.random()
        if coin_toss < 0.5 :
            tails += 1
        else:
            heads += 1
    heads_percentage = (heads / num_of_flips) * 100
    tails_percentage = (tails / num_of_flips) * 100

    return heads_percentage, tails_percentage

num_of_flips = int(input("Enter number of coin flips: "))

heads_percentage, tails_percentage = coin_flip(num_of_flips)

print(f'heads percentage: {heads_percentage} and tails percentage: {tails_percentage}')