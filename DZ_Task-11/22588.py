from math import *

for V in range(1, 10_000):
    L = 18
    N = 10 + 36 + 36 + 70
    i = ceil(log2(N))
    I = (L * i / 8) + V
    if 2000 * I <= 100 * 2 ** 10:
        print(V)

# 33