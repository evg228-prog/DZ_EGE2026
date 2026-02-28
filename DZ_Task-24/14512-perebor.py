with open(r'.\files\24_14512.txt') as file:
    data = file.readline()

data = data.replace('1', '1 1')
data = data.replace('8', '8 8')
data = data.split()

ans = 0

for line in data:
    if line[0] != line[-1] and line.count('B') == line.count('C'):
        ans = max(ans, len(line))

print(ans)

# 1315