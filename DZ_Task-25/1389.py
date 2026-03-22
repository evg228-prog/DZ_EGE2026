def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and is_prime(i):
            d.add(i)
        if num % (num // i) == 0 and is_prime(num // i):
            d.add(num // i)
    return sum(d)

cnt = 0

for N in range(250_001, 10 ** 15):
    S = f(N)
    if S != 0 and S % 17 == 0:
        print(N, S)
        cnt += 1
        if cnt == 5:
            break