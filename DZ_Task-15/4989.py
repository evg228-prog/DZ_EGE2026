def DEL(n, m):
    return n % m == 0

def f(A):
    for x in range(1, 1000):
        B = 20 <= x <= 80
        F = (not B) or (not DEL(x, 17)) or (A[0] <= x <= A[1])
        if not F:
            return False
    return True

ans = float('inf')
for p in range(1, 1000):
    for n in range(p, 1000):
        A = (p, n)
        if f(A):
            ans = min(ans, n - p)

print(ans)

# 34