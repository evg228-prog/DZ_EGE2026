with open (r'.\files\26.2_19727.txt') as file:
    M, N = map(int, file.readline().split())
    cans = [int(i) for i in file]

cans = sorted(cans)

ans = []

for can in cans:
    if sum(ans) + can <= M:
        ans.append(can)

free_space = M - sum(ans[:-1])

print(len(ans), len([i for i in cans if i > free_space]))

# 162 788
