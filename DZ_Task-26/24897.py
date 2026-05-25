with open(r'.\files\26_24897.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data, key=lambda x: (x[1], x[2], x[0]))

clean = []
for id, house, entrance in data:
    if not clean or clean[-1][1] != house or clean[-1][2] != entrance:
        clean.append([id, house, entrance])

best_house = 0
best_start = 0
best_len = 0
best_id = 10**18

cur_house = clean[0][1]
cur_start = clean[0][2]
cur_len = 1
cur_id = clean[0][0]

for i in range(1, len(clean)):
    id, house, entrance = clean[i]
    prev_id, prev_house, prev_entrance = clean[i - 1]
    if house == cur_house and entrance == prev_entrance + 1:
        cur_len += 1
    else:
        if cur_len > best_len:
            best_house = cur_house
            best_start = cur_start
            best_len = cur_len
            best_id = cur_id
        elif cur_len == best_len and cur_id < best_id:
            best_house = cur_house
            best_start = cur_start
            best_len = cur_len
            best_id = cur_id
        cur_house = house
        cur_start = entrance
        cur_len = 1
        cur_id = id

if cur_len > best_len:
    best_house = cur_house
    best_start = cur_start
    best_len = cur_len
    best_id = cur_id
elif cur_len == best_len and cur_id < best_id:
    best_house = cur_house
    best_start = cur_start
    best_len = cur_len
    best_id = cur_id

print(best_house, best_start)

# 503 805