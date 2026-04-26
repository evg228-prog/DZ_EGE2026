from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_A_29075.txt') as file:
    dots = []
    target =[]
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:].strip() == 'III':
            target.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 8]
cluster_2 = [d for d in dots if d[1] < 8]

target_1 = [d for d in target if d[1] > 8]
target_2 = [d for d in target if d[1] < 8]

if len(target_1) < len(target_2):
    minn = center(cluster_1)[0]
else:
    minn = center(cluster_2)[0]

if len(target_1) > len(target_2):
    maxx = center(cluster_1)[1]
else:
    maxx = center(cluster_2)[1]

print(minn * 10_000, maxx * 10_000)

# 70391 61225