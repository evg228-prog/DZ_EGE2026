from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27A_27138.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 2
clusters = []
while dots:
    cluster =[dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters += [cluster]
print([len(cluster) for cluster in clusters])
centers_X = [center(cluster)[0] for cluster in clusters]
centers_Y = [center(cluster)[1] for cluster in clusters]
print(abs(centers_X[0] - centers_X[1]) * 10_000, abs(centers_Y[0] - centers_Y[1]) * 10_000)

# 279051 449883
