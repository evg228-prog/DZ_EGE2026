with open(r'.\files\23193.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 1, 1, 3]:
        rep = [i for i in line if line.count(i) > 1]
        non_rep = [i for i in line if line.count(i) == 1]
        if rep[0] > sum(non_rep) / len(non_rep):
            print(pos, line)

# 10493