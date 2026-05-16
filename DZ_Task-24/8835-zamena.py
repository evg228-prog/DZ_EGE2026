with open(r'files/24_8835.txt') as file:
    data = file.readline()

data = data.replace('.', '.*')
data = data.split('*')

ans = 0
for line in data:
    if line.count('M') == 112:
        ans = max(ans, len(line))
print(ans)

# Ответ: 0 ?!