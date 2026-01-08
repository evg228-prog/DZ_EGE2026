with open(r'.\files\24_11813.txt') as file:
    data = file.readline()

for i in 'EYUIOA':
    data = data.replace(i, '*')
    if i != '*':
        data = data.replace(i, '+')
if data[i] == '*' and data[i - 1] == '+':
        print(len(max(data, key=len)))