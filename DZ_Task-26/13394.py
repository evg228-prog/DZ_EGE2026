from math import *

with open(r'.\files\26.6_13394.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)
sale_prices = [i for i in prices if i > 350]

k = 3
one_bill = sum(prices) - floor(sum(sale_prices[- len(sale_prices) // k:]) * 0.75)
many_bills = sum(prices) - sum(floor(i * 0.75) for i in sale_prices[k - 1::k])

print(many_bills, one_bill)

# 3924309 4275729
