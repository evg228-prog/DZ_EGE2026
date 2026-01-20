from itertools import *
def f(A):
    for x, y in product(range(0, 1000), repeat=2):
        B = 50 <= x <= 70
        F = (2 * x + y != 150) or (not B) or (A > y)
        if not F:
            return False
    return True

for A in range(0, 1000):
    if f(A):
        print(A)
        break

# 51