with open(r'.\files\24_23381.txt') as file:
    data = file.readline()

ans = 0

for i in range(len(data)):
    if data[i] not in '02468':
        continue
    if i + 1 >= len(data) or not data[i + 1].isalpha():
        continue
    letter = data[i + 1]
    cnt = 2
    for j in range(i + 2, len(data)):
        if data[j] == letter:
            cnt += 1
        elif data[j] in '02468':
            cnt += 1
            break
        else:
            break
    ans = max(ans, cnt)
print(ans)

# 1212
