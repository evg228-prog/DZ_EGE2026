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
            d |= {i, num // i}
    return sum(d)

cnt = 0
for N in range(1_273_548, 10**10):
    M = f(N)
    if is_prime(M % 100_000):
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

# 1273566 1637537
# 1273570 1139869
# 1273578 1287317
# 1273582 651769
# 1273590 2225609