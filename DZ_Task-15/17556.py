def DEL(n, m):
    return n % m == 0

def f(A):
    for x in range(1, 1000):
        B = 70 <= x <= 90
        F = DEL(x, A) or (B <= (not DEL(x, 22)))
        if not F:
            return False
    return True

for A in range(1, 1000):
    if f(A):
        print(A)

# 88