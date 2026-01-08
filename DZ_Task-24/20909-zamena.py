with open(r'.\files\24_20909.txt') as file:
    data = file.readline()

data = data.split('AB')
ans = 0
for i in range(len(data) - 100):
    text = 'AB'.join(data[i:i + 101])
    ans = max(ans, len(text))
print(ans)