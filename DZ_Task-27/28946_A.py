from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_A_28946.txt') as file:
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
    if len(cluster) > 20:
        clusters += [cluster]
max_cluster = max(clusters, key=len)
center_1 = center(max_cluster)
cnt = sum(d[1] < center_1[1] for d in max_cluster)

min_cluster = min(clusters, key=len)
center_2 = center(min_cluster)

print(cnt, abs(center_1[0] - center_2[0]) * 10_000)

# 173 27601