with open(r'.\files\26-DV-new_type.txt') as file:
    N, K = map(int, file.readline().split())
    data = []
    for line in file:
        time, ID, S = line.split()
        time = list(map(int, time.split(':')))
        time = (time[0] * 60 + time[1]) * 60 + time[2]
        data.append([time, int(ID), int(S)])

data = sorted(data)
copies_before_12 = []
disk = 0
clients = {}
for time, ID, S in data:
    if ID in clients:
        clients[ID] += S
    else:
        clients[ID] = S
    if disk + S <= K:
        disk += S
    else:
        if time < 12 * 60 * 60:
            copies_before_12.append(disk)
        disk = S
print(max(clients, key=lambda x: clients[x]), sum(sorted(copies_before_12)[-2:]))

# 5433 99961