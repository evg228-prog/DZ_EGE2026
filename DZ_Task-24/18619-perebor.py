with open(r'.\files\24_18619.txt') as file:
    data = file.readline()

ans = 0

for i in range(len(data)):
    if data[i] == 'B':
        cnt = 1
        Flag = True
        for j in range(i + 1, len(data)):
            if data[j] in '123456':
                cnt += 1
                Flag = False
                ans = max(ans, cnt)
            elif data[j] in '-*':
                if Flag:
                    break
                cnt += 1
                Flag = True
            else:
                break
print(ans)