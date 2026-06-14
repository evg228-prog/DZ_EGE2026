def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0 and is_prime(i):
            d.add(i)
        if num % (num // i) == 0 and is_prime(num // i):
            d.add(num // i)
    if len(d) > 1:
        return d
    return 0

cnt = 0
for N in range(7_800_001, 10 ** 12):
    M = f(N)
    if M != 0 and (max(M) + min(M)) % 100 == 63 and (max(M) + min(M)) % len(M) == 0:
        print(N, (max(M) + min(M)))
        cnt += 1
        if cnt == 5:
            break

# 7800610 780063
# 7801042 8463
# 7801312 1863
# 7801916 8163
# 7802032 69663