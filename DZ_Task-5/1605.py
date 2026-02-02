ans = []
for N in range(1, 1000):
    R = f'{2 + N:b}'
    OSTAT = sum(map(int, R)) % 2
    R = R + str(OSTAT)
    R = R + str(sum(map(int, R + str(OSTAT))) % 2)
    R = int(R, 2)
    if R < 61:
        ans.append(N)
print(max(ans))

# 13