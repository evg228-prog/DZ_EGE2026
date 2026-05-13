with open(r'.\files\24_15339.txt') as file:
    data = file.readline()

for i in 'ABC': data = data.replace(i, '*')
for i in '6789': data = data.replace(i, '#')

while '**' in data and '##' in data:
    data = data.replace('**', '* *')
    data = data.replace('##', '# #')

data = data.split()
print(max(len(x) for x in data))

# 22