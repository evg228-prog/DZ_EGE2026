from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_B_28766.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z' and data[2:].strip() == 'I':
            target.append(list(map(float, [x, y])))

cluster_1 = [
    [d for d in dots if d[1] > 22],
    [d for d in target if d[1] > 22]
]

cluster_2 = [
    [d for d in dots if 16 < d[1] < 22],
    [d for d in target if 16 < d[1] < 22]
]

cluster_3 = [
    [d for d in dots if d[0] > 22],
    [d for d in target if d[0] > 22]
]

clusters = [cluster_1, cluster_2, cluster_3]

B1 = min(
    [dist(d1, d2) for d1 in cluster_1[1] for d2 in cluster_1[1] if d1 != d2] +
    [dist(d1, d2) for d1 in cluster_2[1] for d2 in cluster_2[1] if d1 != d2] +
    [dist(d1, d2) for d1 in cluster_3[1] for d2 in cluster_3[1] if d1 != d2]
)

print(B1 * 10_000)

min_cluster = center(min(clusters, key=lambda x: len(x[1]))[0])
max_cluster = center(max(clusters, key=lambda x: len(x[1]))[0])

B2 = dist(min_cluster, max_cluster)

print(B2 * 10_000)

# 1035 125591