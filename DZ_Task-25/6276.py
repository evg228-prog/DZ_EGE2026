from fnmatch import fnmatch

for N in range(11111111 - 11111111 % 2023, 10**10, 2023):
    if fnmatch(str(N), '1?1?1?1*1') and sum(map(int, str(N))) == 22:
        print(N)

# 19131511
# 1012141291
# 1319111311
# 1516111051