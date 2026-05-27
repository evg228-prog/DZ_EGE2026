from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_A_29080.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[:2] == 'L3':
            target.append(dots[-1])

cluster_1 = [d for d in dots if d[1] < 8]
cluster_2 = [d for d in dots if d[1] > 8]

target_1 = [d for d in target if d[1] < 8]
target_2 = [d for d in target if d[1] > 8]
targets = [target_1, target_2]

if len(cluster_1) < len(cluster_2):
    minn = center(cluster_1)
    maxx = center(cluster_2)
else:
    minn = center(cluster_2)
    maxx = center(cluster_1)

A1 = max(dist(minn, d) for line in targets for d in line)
A2 = max(dist(maxx, d) for line in targets for d in line)
print(A1 * 10_000, A2 * 10_000)

# 73624 70820