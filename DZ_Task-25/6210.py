from fnmatch import fnmatch
def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return d

for N in range(212, 10**7, 53):
    M = f(N)
    if fnmatch(str(N), '*2?2*') and str(N) == str(N)[::-1] and len(M) > 30:
        print(N, sum(M))

# 212212 508032
# 2527252 5588352
# 4282824 13789440
# 4626264 11787120
# 8125218 19595520
# 8824288 19908504