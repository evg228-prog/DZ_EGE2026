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
    return d

cnt = 0
for N in range(5_000_001, 10**11):
    dels = fact(N)
    if N % 100 == 12 and sum(dels.count(x) == 5 for x in dels) >= 1:
        print(N, min(x for x in dels if dels.count(x) == 5))
        cnt += 1
        if cnt == 5:
            break

# 5001312 2
# 5001912 3
# 5002912 2
# 5004512 2
# 5006112 2