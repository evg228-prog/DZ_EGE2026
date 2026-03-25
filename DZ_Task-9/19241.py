with open(r'.\files\19241.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 3, 3]:
        rep = [i for i in set(line) if line.count(i) != 1]
        non_rep = [i for i in set(line) if line.count(i) == 1]
        if sum(rep) / len(rep) < non_rep[0]:
            print(pos)

# 17975