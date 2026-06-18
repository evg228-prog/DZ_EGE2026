def DEL(n, m):
    return n % m == 0

def f(x):
    C = 30 <= x <= 45
    return (DEL(x, A) and C) <= (not DEL(x, 12))

for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break

# 5