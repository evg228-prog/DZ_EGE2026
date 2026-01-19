def DEL(n, m):
    return n % m == 0

def f(A):
    for x in range(1, 1000):
        B = 70 <= x <= 80
        F = DEL(x , 12) and B and (not DEL(x, A))
        if F:
            return False
    return True

cnt = 0
for A in range(1, 1000):
    if f(A):
        cnt += 1
print(cnt)

# 12