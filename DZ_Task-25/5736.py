def f(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return d

cnt = 0
for N in range(10 ** 9 + 1, 10**14):
    if str(N) == str(N)[::-1]:
        F = f(N)
        if max(F) % 7 == 0:
            print(N, max(F))
            cnt += 1
            if cnt == 5:
                break

# 1001771001 333923667
# 1002002001 334000667
# 1003003001 143286143
# 1004774001 334924667
# 1005005001 335001667