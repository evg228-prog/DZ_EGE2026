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

cnt = 0
for N in range(7_305_679, 10**10):
    dels = fact(N)
    if len(dels) == 4  and str(sum(dels)) == str(sum(dels))[::-1]:
        print(N, sum(dels))
        cnt += 1
        if cnt == 5:
            break

# 7305747 2002
# 7305818 16561
# 7305986 545
# 7306057 696
# 7306059 606