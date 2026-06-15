with open(r'.\files\24_19254 (1).txt') as file:
    data = file.readline()

data = data.replace('FSRQ', 'FS RQ')
data = data.split()

ans = 0

for i in range(len(data) - 80):
    line = 'RQFS'.join(data[i:i + 81])
    ans = max(ans, len(line))

print(ans)
