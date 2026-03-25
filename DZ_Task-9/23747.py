with open(r'.\files\23747.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = []
for pos, line in enumerate(data, start=1):
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 1, 1, 1, 3]:
        rep = [i for i in set(line) if line.count(i) != 1]
        non_rep = [i for i in set(line) if line.count(i) == 1]
        if sum(non_rep) / len(non_rep) <= rep[0]:
            ans.append([pos, sum(line)])
print(max(ans))

# 901