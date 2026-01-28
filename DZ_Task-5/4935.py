ans = []
for N in range(1, 100_000):
    R = f'{N:b}'
    if sum(map(int, R)) % 2 == 0:
        R = '10' + R[:-2] + '00'
    else:
        R = '11' + R[:-2] + '11'
    R = int(R, 2)
    if N < 30:
        ans.append(R)
print(max(ans))

# 127