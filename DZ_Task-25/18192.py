def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and is_prime(i):
            d.add(i)
        if num % (num // i) == 0 and is_prime(num // i):
            d.add(num // i)
    if len(d) == 3:
        return max(d)
    return False

cnt = 0

for N in range(1_000_001, 10 ** 15):
    M = f(N)
    if M:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

# 1000002 166667
# 1000004 89
# 1000006 71429
# 1000012 19231
# 1000013 383