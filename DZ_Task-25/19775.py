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
            if is_prime(i) and i != num: d |= {i}
            if is_prime(num // i) and num // i != num: d |= {num // i}
    if len(d) > 1:
        return sum(d)
    return 0
cnt = 0
for N in range(32_500_001, 10**20):
    S = f(N)
    if S != 0 and S % 145 == 0:
        print(N, S)
        cnt += 1
        if cnt == 7:
            break

# 32500280 2755
# 32500301 58290
# 32500440 1450
# 32500623 17545
# 32500665 722245
# 32500700 7975
# 32500834 4785