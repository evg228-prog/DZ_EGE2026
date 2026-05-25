with open(r'.\files\24346.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    u1 = sum(1 for i in line if line.count(i) > 1) > 0 and sum(1 for i in line if line.count(i) == 1) > 0
    u2 = sum(i for i in line if line.count(i) > 1) ** 2 > sum(i for i in line if line.count(i) == 1) ** 2
    u3 = sum(line) % 2 != 0
    if u1 and u2 and u3:
        print(pos)

# 2671