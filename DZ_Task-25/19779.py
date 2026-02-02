def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i % 1000 == 777 and is_prime(i):
                d |= {i}
            if (num // i) % 1000 == 777 and is_prime(num // i):
                d |= {num // i}
    if d:
        return min(d)
    return 0

cnt = 0
for N in range(55_000_001, 10**10):
    F = f(N)
    if F:
        print(N,  F)
        cnt += 1
        if cnt == 4:
            break

# 55000662 9166777
# 55001262 2777
# 55001554 27500777
# 55001704 1777



