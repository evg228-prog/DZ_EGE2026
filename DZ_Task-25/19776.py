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
        if num % i == 0 and is_prime(num // i):
            d.add(num // i)
    if len(d) > 1:
        return max(d) + min(d)
    return 0

cnt = 0
for N in range(23_600_001, 10 ** 10):
    M = f(N)
    if M % 213 == 171:
       print(N, M)
       cnt += 1
       if cnt == 6:
           break

# 23600182 694125
# 23600442 28713
# 23600478 357585
# 23600570 1449
# 23600838 135639
# 23600970 29139