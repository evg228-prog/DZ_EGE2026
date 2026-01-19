from itertools import *
def f(A):
    for x, y, z in product(range(1, 1000), repeat=3):
        F = (2 * x + y != 136) or (z * y < 100) or (A * A >= x + y)
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)

# 12