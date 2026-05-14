with open(r'.\files\24_8510.txt') as file:
    data = file.readline()

data = data.replace('NN', 'N N')
data = data.replace('PP', 'P P')
data = data.replace('OO', 'O O')
data = data.replace('NO', 'N O')
data = data.replace('NP', 'N P')
data = data.replace('PN', 'P N')
data = data.replace('PO', 'P O')
data = data.replace('ON', 'O N')
data = data.replace('OP', 'O P')

data = data.split()
print(len(max(data, key=len)))

# 57