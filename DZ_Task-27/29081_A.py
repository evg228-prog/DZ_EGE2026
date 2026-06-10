from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_A_29081.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data == 'VII':
            target.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 8]
cluster_2 = [d for d in dots if d[1] < 8]

target_1 = [d for d in target if d[1] > 8]
target_2 = [d for d in target if d[1] < 8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
A1 = min(
    min(dist(center_1, d) for d in target_1),
    min(dist(center_2, d) for d in target_2),
)

A2 = max(
    max(dist(center_1, d) for d in target_1),
    max(dist(center_2, d) for d in target_2),
)

print(A1 * 10_000, A2 * 10_000)

# 1495 16955