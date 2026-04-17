from math import *

def anticenter(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return max(res)[1]

with open(r'.\files\27A_27590.txt') as file:
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
anticenters = [anticenter(cluster) for cluster in clusters]
anticenter_A_min = anticenter(min(clusters, key=len))
anticenter_A_max = anticenter(max(clusters, key=len))
print(sum(anticenter_A_min) * 10_000, sum(anticenter_A_max) * 10_000)

# 210816 82076

with open(r'.\files\27B_27590.txt') as file:
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
anticenters = [anticenter(cluster) for cluster in clusters]
anticenter_X = max(anticenter(cluster)[0] for cluster in clusters)
anticenter_Y = min(anticenter(cluster)[1] for cluster in clusters)
print(anticenter_X * 10_000, anticenter_Y * 10_000)

# 231257 157454