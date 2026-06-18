def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 0:
        return [i for i in d if i % 10 == 7 and i != 7]
    return 0

cnt = 0
for N in range(700_001, 10**10):
    M = f(N)
    if M:
        print(N, min(M))
        cnt += 1
        if cnt == 5:
            break

# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167