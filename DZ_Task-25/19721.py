def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) == 4:
        return d
    return 0

for N in range(178965, 178983):
    if f(N):
        print(*sorted(f(N), reverse=True))

# 178967 937 191 1
# 178977 59659 3 1
# 178979 2011 89 1
# 178982 89491 2 1
