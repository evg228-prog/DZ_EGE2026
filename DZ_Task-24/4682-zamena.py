with open(r'.\files\24_4682.txt') as file:
    data = file.readline()

for i in 'AE': data = data.replace(i, '*')
for i in 'BCD': data = data.replace(i, '#')

data = data.replace('*#', '+')
data = data.replace('*', ' ')
data = data.replace('#', ' ')

data = data.split()

print(len(max(data, key=len)))

##################################################

vowels = 'EYUIOA'

for i in data:
    if i in vowels:
        data = data.replace(i, '*')
    else:
        data = data.replace(i, '#')

data = data.replace('*#', '+')
data = data.replace('*', ' ')
data = data.replace('#', ' ')

data = data.split()

print(len(max(data, key=len)))

# 202