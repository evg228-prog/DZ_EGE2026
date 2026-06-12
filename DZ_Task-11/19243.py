from math import *

for N in range(1, 100_000):
    i = ceil(log2(N))
    L = 377
    I = ceil(L * i / 8)
    if 23_155 * I > 5536 * 2**10:
        print(N)
        break