with open(r'.\files\24_16388.txt') as file:
    data = file.readline()

data = data.replace('KLMN', '****')
data = data.replace('LMN*', ' ****')
data = data.replace('MN*', ' ***')
data = data.replace('N*', ' **')
data = data.replace('KLM*', '**** ')
data = data.replace('LM*', '*** ')
data = data.replace('M*', '** ')
for i in 'KLMN': data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))

# 182