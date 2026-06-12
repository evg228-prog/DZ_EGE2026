def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i < num + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]
    if len(d) == len(set(d)) == 2:
        a, b = sorted(d)
        if all(not is_prime(i) for i in range(a + 1, b)):
            return sum(d)
    return []

cnt = 0
for N in range(3_700_001, 10 ** 11):
    M = fact(N)
    if M:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

# 3732623 3864
# 3767417 3882
# 3802499 3900
# 3849323 3924
# 3904567 3952