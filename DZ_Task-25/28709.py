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
        while num % i == 0 and is_prime(i):
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]
    if len(d) == 3:
        return d
    return 0

cnt = 0

for N in range(6_300_001, 10 ** 15):
    dels = fact(N)
    if dels:
        if all('3' in str(x) or '4' in str(x) for x in dels):
            print(N, max(dels))
            cnt += 1
            if cnt == 5:
                break

# 6300051 2503
# 6300057 39623
# 6300069 1543
# 6300087 9013
# 6300101 4153