with open(r'.\files\17968.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for line in data:
    if max(line) < sum(line) - max(line):
        if sum(i for i in line if i % 2 == 0) == sum(i for i in line if i % 2 != 0):
            ans += 1
print(ans)

# 13