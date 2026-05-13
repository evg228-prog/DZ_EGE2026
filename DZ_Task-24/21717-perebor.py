with open(r'.\files\24_21717.txt') as file:
    data = file.readline()

pos = []
for i in range(len(data) - 2):
    if data[i:i + 3] == 'RSQ':
        pos.append(i)

ans = 10 ** 10
for i in range(len(pos) - 129):
    start = pos[i]
    end = pos[i + 129] + 2
    j = end + 1
    while j < len(data) and data[j] == 'Q':
        j += 1
    if j < len(data):
        line = j - start + 1
        ans = min(ans, line)
print(ans)

# 497
