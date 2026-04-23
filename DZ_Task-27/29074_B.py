from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_B_29074.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[2:].strip() == 'V':
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

B1 = min(
    [dist(center(cluster_1[0]), d1) for d1 in cluster_1[1]] +
    [dist(center(cluster_2[0]), d1) for d1 in cluster_2[1]] +
    [dist(center(cluster_3[0]), d1) for d1 in cluster_3[1]]
)

B2 = max(
    [dist(center(cluster_1[0]), d1) for d1 in cluster_1[1]] +
    [dist(center(cluster_2[0]), d1) for d1 in cluster_2[1]] +
    [dist(center(cluster_3[0]), d1) for d1 in cluster_3[1]]
)

print(B1 * 10_000, B2 * 10_000)

# 1738 20765