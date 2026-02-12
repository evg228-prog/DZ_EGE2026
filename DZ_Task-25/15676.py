from fnmatch import fnmatch

def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return d

for N in range(4, 100_000):
    if f(N):
        for i in range(1, 10**8, 22768):
            if fnmatch(str(i), f'1{N}03*6*'):
                print(i, N)