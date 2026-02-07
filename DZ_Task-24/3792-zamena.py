with open(r'.\files\24_3792.txt') as file:
    data = file.readline()

for i in 'ABC': data = data.replace(i, '*')
for i in data:
    if i != '*': data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))

# 16