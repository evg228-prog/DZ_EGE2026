with open(r'.\files\14250.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for pos, line in enumerate(data, start=1):
    if len(line) == len(set(line)):
        if (max(line) - min(line)) ** 3 >= (sum(line) - max(line) - min(line)) ** 2:
            cnt += pos
print(cnt)

# 57879735