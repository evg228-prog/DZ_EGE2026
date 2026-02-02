from math import prod
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i): d += [i]
            if is_prime(num // i): d += [num // i]
    if len(d) == 12 and prod(d) == num:
        return max(d)
    return 0

cnt = 0
for N in range(24_517_513, 10**10):
    F = f(N)
    if F:
        print(N, F)
        cnt += 1
        if cnt == 5:
            break

all_primes = []
for i in range(2, int(24_517_512 ** 0.5) + 1):
    if is_prime(i):
        all_primes.append(i)
print(len(all_primes))

# Долго работает
