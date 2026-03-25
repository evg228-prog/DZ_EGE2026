with open(r'.\files\21704.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data:
    if line == sorted(line, reverse=True):
        if (max(line) + min(line)) / 2 > (sum(line) - max(line) - min(line)) / 5:
            print(sum(line))
            break

# 652
