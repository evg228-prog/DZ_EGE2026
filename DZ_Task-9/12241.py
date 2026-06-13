with open(r'.\files\12241.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for line in data:
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 2, 2, 2]:
        rep = [i for i in set(line) if line.count(i) > 1]
        non_rep = [i for i in set(line) if line.count(i) == 1]
        if (max(rep) + min(rep)) / 2 < non_rep[0]:
            ans += 1
print(ans)

# 3382