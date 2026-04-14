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

for N in range(3_600_001, 10 ** 15):
    dels = fact(N)
    if dels:
        if all('3' in str(x) and '5' in str(x) for x in dels):
            print(N, max(dels))
            cnt += 1
            if cnt == 5:
                break

# 4081477 1453
# 4278107 1523
# 4300579 1531
# 4334287 1543
# 4362377 1553