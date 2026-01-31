def DEL(n, m):
    return n % m == 0

def f(x):
    B = 50 <= x <= 70
    return DEL(x, A) or (B <= (not DEL(x, 16)))

for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break

# 64