def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i): d.add(i)
            if is_prime(num // i): d.add(num // i)
    if len(d) > 1:
        return max(d) - min(d)
    return 0

cnt = 0
for N in range(3_333_338, 10**14):
    R = f(N)
    if R > 1000 and R % 3 == 0:
        print(N, R)
        cnt += 1
        if cnt == 5:
            break