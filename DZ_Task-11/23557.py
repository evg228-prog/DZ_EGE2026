from math import *

for L in range(1, 10_000):
    N = 552
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 45_877 * I > 49 * 2 ** 20:
        print(L)
        break

# 896