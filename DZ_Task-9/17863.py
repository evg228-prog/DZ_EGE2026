with open(r'.\files\17863.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for line in data:
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 1, 1, 3]:
        rep = [i for i in set(line) if line.count(i) != 1]
        non_rep = [i for i in set(line) if line.count(i) == 1]
        if (rep[0] * 3) ** 2 > sum(non_rep) ** 2:
            ans += 1
print(ans)

# 273