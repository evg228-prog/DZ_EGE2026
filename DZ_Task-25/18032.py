def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return sum(d)

for N in range(1000, 10000):
    F = f(N)
    if F % 100 == 23:
        print(N, F)

# 1681 1723
# 1936 4123
# 2592 7623
# 3025 4123
# 6962 10623
# 7569 11323

