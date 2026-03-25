with open(r'.\files\1962.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for line in data:
    cnt = [int(i) for i in line]
    if (cnt[0] + cnt[1] > cnt[2]) and (cnt[0] + cnt[2] > cnt[1]) and (cnt[1] + cnt[2] > cnt[0]):
        ans += 1
print(ans)

# 2453