def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 1:
        return max(d) + min(d)
    return 0

cnt = 0
for N in range(800_001, 10**29):
    M = f(N)
    if M % 10 == 4:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

# 800004 400004
# 800009 114294
# 800013 266674
# 800024 400014
# 800033 61554