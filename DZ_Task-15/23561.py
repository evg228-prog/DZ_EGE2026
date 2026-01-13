def DEL(n, m):
    return n % m == 0

def f(A):
    for x in range(1, 1000):
        F = DEL(x, 128) <= ((not DEL(x, A)) <= (not DEL(x, 80)))
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)

# 640