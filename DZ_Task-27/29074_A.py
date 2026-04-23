with open(r'.\files\27_A_29074.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z':
            target.append(list(map(float, [x, y])))

target_1 = [d for d in target if d[1] > 8]
target_2 = [d for d in target if d[1] < 8]

print(len(target_1), len(target_2))

