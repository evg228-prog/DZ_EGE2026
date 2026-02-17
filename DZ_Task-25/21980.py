def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if is_prime(i) and i % 10 == 7: d.add(i)
            if is_prime(num // i) and (num // i) % 10 == 7: d.add(num // i)
    if len(d) > 1:
        return sum(d) // len(d)
    return 0

cnt = 0
for N in range(1, 750_000)[::-1]:
    F = f(N)
    if F != 0 and F % 111 == 0:
        print(N, F)
        cnt += 1
        if cnt == 5:
            break

# 749039 7992
# 748679 3552
# 748663 333
# 746360 222
# 745109 2997