with open(r'.\files\24_22356.txt') as file:
    data = file.readline()

ans = []
checkpoint = 0
for i in range(len(data)):
    if i < checkpoint:
        continue
    if data[i] in '123456789AB':
        num = ''
        for j in range(i, len(data)):
            if data[j] in '0123456789AB':
                num += data[j]
            else:
                checkpoint = j
                break
            if int(data[j], 36) % 2 != 0:
                ans.append((len(num), num, i))
print(max(ans, key=lambda x: (x[0], x[1]))[2])

# 8499457