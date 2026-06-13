from math import *

for N in range(1, 100_000)[::-1]:
    L = 257
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 295_740 * I <= 33 * 2 ** 20:
        print(N)
        break

# 8