with open(r'.\files\24_23206.txt') as file:
    data = file.readline()

for i in '02468': data = data.replace(i, ' 0')
data = data.split()

ans = []
for i in data:
    if i[0] == '0':
        if i.count('S') == 35:
            ans.append(len(i))
        elif i.count('S') > 35:
            while i.count('S') > 35:
                pos_S = i.rfind('S')
                i = i[:pos_S]
            ans.append(len(i))
print(max(ans))

# 292