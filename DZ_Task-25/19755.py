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
            if is_prime(i): d |= {i}
            if is_prime(num // i): d |= {num // i}
    if len(d) > 1:
        return min(d) + max(d)
    return 0

cnt = 0
for N in range(1_200_001, 10**15):
    M = f(N)
    if M > 2000 and M % 10 == 8:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

# 1200005 2248
# 1200011 2388
# 1200037 17978
# 1200067 109108
# 1200197 2598
