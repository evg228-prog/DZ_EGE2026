from math import *

def center(cluster):
    res = []
    for d1 in cluster:
        sum_dist = sum(dist(d1, d2) for d2 in cluster)
        res.append([sum_dist, d1])
    return min(res)[1]

with open(r'.\files\27_A_29076.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] == '2':
            target.append(dots[-1])

cluster_1 = [d for d in dots if d[1] > 8]
cluster_2 = [d for d in dots if d[1] < 8]

target_1 = [d for d in target if d[1] > 8]
target_2 = [d for d in target if d[1] < 8]

if min(target_1, target_2, key=len) == target_1:
    minn = center(cluster_1)
    maxx = center(cluster_2)
else:
    minn = center(cluster_2)
    maxx = center(cluster_1)

print(minn[0] * 10_000, maxx[1] * 10_000)

# 70391 61225