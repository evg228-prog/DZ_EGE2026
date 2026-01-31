def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    d_7 = []
    for i in sorted(d):
        if i != 7 and i % 10 == 7:
            d_7 += [i]

    if d_7:
        return min(d_7)
    return 0

cnt = 0
for N in range(700_001, 10**14):
    F = f(N)
    if F:
        print(N, F)
        cnt += 1
        if cnt == 5:
            break

# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167