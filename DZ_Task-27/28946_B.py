from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_B_28946.txt') as file:
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
min_cluster = min(clusters, key=len)
x_c, y_c = center(min_cluster)
cnt = sum(abs(x - x_c) <= 0.9 and abs(y - y_c) <= 0.9 for x, y in min_cluster)

clusters = sorted(clusters, key=len)
center_1 = center(clusters[1])
center_2 = center(clusters[2])

print(cnt, abs(center_1[1] - center_2[1]) * 10_000)

# 89 107171

