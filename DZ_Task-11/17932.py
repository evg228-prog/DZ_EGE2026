from math import *

for N in range(1, 1000)[::-1]:
    L = 211
    i = ceil(log2(N))
    I = ceil(i * L / 8)
    if I * 23654 <= 3241 * 2 ** 10:
        print(N)
        break

# 32