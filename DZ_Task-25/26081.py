def f(num):
    for N in range(113, num, 226):
        if N % 2 != 0:
            for i in range(1, 14):
                if N + 3 ** i == num:
                    return i
    return 0

cnt = 0
for M in range(100_000, 1_000_000, 2):
    if '0' not in str(M):
        F = f(M)
        if F:
            print(M, F)
            cnt += 1
            if cnt == 5:
                break

# 111142 10
# 111232 7
# 111312 8
# 111314 2
# 111322 5