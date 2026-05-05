with open(r'.\files\24_7624.txt') as file:
    data = file.readline()

data = data.replace('XY', 'X Y')
data = data.replace('XZ', 'X Z')
data = data.replace('XX', 'X X')
data = data.replace('YX', 'Y X')
data = data.replace('YZ', 'Y Z')
data = data.replace('YY', 'Y Y')
data = data.replace('ZY', 'Z Y')
data = data.replace('ZX', 'Z X')
data = data.replace('ZZ', 'Z Z')

data = data.split()

print(len(max(data, key=len)))

######################################################

answer = data[0]

for i in range(1, len(data)):
    if data[i - 1] in 'XYZ' and data[i] in 'XYZ':
        answer += ' '
    answer += data[i]

answer = answer.split()

print(len(max(answer, key=len)))


# 786