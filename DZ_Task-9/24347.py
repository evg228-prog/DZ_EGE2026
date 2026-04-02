with open(r'.\files\24347.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0

for line in data:
    u1 = line.count(max(line)) == 1
    u2 = line[0] not in (max(line), min(line)) and line[-1] not in (max(line), min(line))
    line = sorted(line)
    u3 = line[-3] * line[-2] * line[-1] % line[0] == 0
    if u1 + u2 + u3 == 1:
        ans += 1
print(ans)

# 2462