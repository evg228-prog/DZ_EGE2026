def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i <= num + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 1:
        d += [num]
    if len(d) == 2:
        return d
    return []

cnt = 0
for N in range(6_651_221, 10 ** 15):
    M = fact(N)
    if M:
        x, y = M
        if str(x).count('2') == 1 and str(y).count('2') == 1:
            print(N, max(x, y))
            cnt += 1
            if cnt == 5:
                break

# 6651241 2579
# 6651262 3325631
# 6651286 3325643
# 6651314 3325657
# 6651347 289189