with open(r'.\files\26_15_23259.txt') as file:
    N, M = map(int, file.readline().split())
    file = file.readlines()
    weights = [int(i) for i in file[:N]]
    sled = [int(i) for i in file[N:]]

weights = sorted(weights)
sled = sorted(sled)
cnt = 0

for w in weights:
    for s in sled.copy():
       if w <= s:
           cnt += 1
           sled.remove(s)
           break

max_weight = 0
for w in weights[::-1]:
    sled = sorted([int(i) for i in file[N:]])
    for s in sled[::-1]:
        if w <= s:
            max_weight = w
    if max_weight:
        break
print(cnt, max_weight)

# 800 450466