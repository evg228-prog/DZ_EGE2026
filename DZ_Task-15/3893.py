def DEL(n, m):
    return m != 0 and n % m == 0

def f(x):
    return DEL(A, 25) and ((DEL(x, 24) and DEL(x, 75)) <= DEL(x, A))

cnt = 0

for A in range(-1000, 1000):
    if all(f(x) for x in range(-1000, 1000)) :
        cnt += 1
print(cnt)

# 16