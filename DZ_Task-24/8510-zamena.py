with open(r'.\files\24_8510.txt') as file:
    data = file.readline()

pairs = ['NN', 'NO', 'NP', 'ON', 'OO', 'OP', 'PN', 'PO', 'PP']

for pair in pairs:
    data = data.replace(pair, pair[0] + ' ' + pair[1])

data = data.split()
ans = max(len(line) for line in data)

print(ans)

# 57