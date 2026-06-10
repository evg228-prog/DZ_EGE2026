with open(r'.\files\23368.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 1, 1, 1, 1]:
        if (min(line) + max(line)) * 2 == (sum(line) - min(line) - max(line)) * 3:
            print(pos)

# 13412