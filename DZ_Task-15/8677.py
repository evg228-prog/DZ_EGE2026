def DEL(n, m):
    return n % m == 0

def f(A):
    for x in range(1, 1000):
        B = 80 <= x <= 100
        F = DEL(x, 17) <= ((not B) or (A < x + 30))
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)

# 114