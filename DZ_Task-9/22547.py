with open(r'.\files\22547.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    if line == sorted(set(line)):
        if sum(1 for i in line if i % 2 == 0) == sum(1 for i in line if i % 2 != 0):
            print(sum(line), pos)

# 335