from math import *

def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if sum(d) % 2 != 0 and prod(d) % 2 != 0 and len(d) > 10:
        return d
    return 0

cnt = 0
for N in range(800_001, 10**11):
    F = f(N)
    if F:
        print(N, len(F))
        cnt += 1
        if cnt == 6:
            break

# 804609 27
# 815409 27
# 826281 15
# 837225 27
# 855625 15
# 859329 15