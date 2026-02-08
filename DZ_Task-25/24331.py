def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i < int(num ** 0.5) + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]
    return d

cnt  = 0
for N in range(13_475_125, 10**15):
    dels = fact(N)
    if len(dels) == 5 and all('5' in str(x) for x in dels):
        print(N, max(dels))
        cnt += 1
        if cnt == 5:
            break

# 13476875 21563
# 13480625 21569
# 13485625 21577
# 13491875 21587
# 13493125 21589