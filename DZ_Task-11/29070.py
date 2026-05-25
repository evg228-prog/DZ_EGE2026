from math import *

for N in range(1, 100_000):
    L1 = 7
    L2 = 9
    cnt_1 = 384
    cnt_2 = 256
    i = ceil(log2(N))
    I1 = ceil(L1 * i / 8) * cnt_1
    I2 = ceil(L2 * i / 8) * cnt_2
    if I1 + I2 == 7168:
        print(N)
        break

# 1025