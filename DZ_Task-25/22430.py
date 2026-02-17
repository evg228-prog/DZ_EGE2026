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
    if len(d) < 4:
        return 0
    sorted_d = sorted(d)
    return sum(sorted(d)[:2] + sorted(d)[-2:])

cnt = 0
for N in range(456_790, 10 ** 10):
    M = f(N)
    if M % 114 == 39:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

# 457366 381
# 457512 1749
# 457638 951
# 457722 495
# 457786 1749