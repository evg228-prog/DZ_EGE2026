def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and i % 2 != 0: d |= {i}
        if num % (num // i) == 0 and (num // i) % 2 != 0: d |= {num // i}
    if len(d) == 3:
        return sorted(d)
    return 0

for N in range(18782, 18823):
    if f(N):
        print(*f(N))

# 5 1879 9395
# 37 127 4699
# 3 1567 4701
# 23 409 9407
# 5 941 4705
# 3 3137 9411

