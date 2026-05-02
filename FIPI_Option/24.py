with open(r'.\files\24_29354.txt') as file:
    data = file.readline()

data = data.split('BC')

ans = 0
for i in range(len(data) - 190):
    if i in [0, len(data) - 191]:
        ans = max(ans, len('BC'.join(data[i:i + 191])) + 0)
    else:
        ans = max(ans, len('BC'.join(data[i:i + 191])) + 2)
print(ans)

# 2287