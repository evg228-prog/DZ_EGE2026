from fnmatch import fnmatch

for N in range(1014513 - 1014513 % 451, 10**9, 451):
    if fnmatch(str(N), '10?451*3'):
        print(N, N // 451)

# 10045123 22273
# 103451733 229383