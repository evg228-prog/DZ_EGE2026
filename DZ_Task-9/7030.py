with open(r'.\files\7030.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for line in data:
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [2, 2, 2]:
        a, b, c = sorted(set(line))
        if a * a + b * b == c * c:
            ans += 1
print(ans)

# 148