from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27A_18678.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters += [cluster]

print([len(cluster) for cluster in clusters])
center_A_X = [center(cluster)[0] for cluster in clusters]
center_A_Y = [center(cluster)[1] for cluster in clusters]
print(sum(center_A_X) / len(center_A_X) * 100_000, sum(center_A_Y) / len(center_A_Y) * 100_000)

# 346070 215898

with open(r'.\files\27B_18678.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters += [cluster]

print([len(cluster) for cluster in clusters])
center_A_X = [center(cluster)[0] for cluster in clusters]
center_A_Y = [center(cluster)[1] for cluster in clusters]
print(sum(center_A_X) / len(center_A_X) * 100_000, sum(center_A_Y) / len(center_A_Y) * 100_000)

# 455364 406022