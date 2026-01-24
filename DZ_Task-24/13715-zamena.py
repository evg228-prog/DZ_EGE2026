with open(r'.\files\24_13715.txt') as file:
    data = file.readline()

data = data.split('AB')

ans = 0
for i in range(len(data) - 50):
    if i in [0, len(data) - 51]:
        ans = max(ans, len('AB'.join(data[i:i + 51])) + 0)
    else:
        ans = max(ans, len('AB'.join(data[i:i + 51])) + 2)
print(ans)