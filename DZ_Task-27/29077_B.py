from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_B_29077.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] in '89':
            target.append(dots[-1])

cluster_1 = [d for d in dots if d[1] > 22]
cluster_2 = [d for d in dots if 16 < d[1] < 22]
cluster_3 = [d for d in dots if d[0] > 22]

target_1 = [d for d in target if d[1] > 22]
target_2 = [d for d in target if 16 < d[1] < 22]
target_3 = [d for d in target if d[0] > 22]

if max(cluster_1, cluster_2, cluster_3, key=len) == cluster_1:
    maxx = target_1
elif max(cluster_1, cluster_2, cluster_3, key=len) == cluster_2:
    maxx = target_2
else:
    maxx = target_3

B1 = len(maxx)

print(B1)

with open(r'.\files\27_B_29077.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] in '0123':
            target.append(dots[-1])

cluster_1 = [d for d in dots if d[1] > 22]
cluster_2 = [d for d in dots if 16 < d[1] < 22]
cluster_3 = [d for d in dots if d[0] > 22]

target_1 = [d for d in target if d[1] > 22]
target_2 = [d for d in target if 16 < d[1] < 22]
target_3 = [d for d in target if d[0] > 22]

B2 = sorted([
    len(target_1),
    len(target_2),
    len(target_3)
])[1]

print(B2)

# 77 28