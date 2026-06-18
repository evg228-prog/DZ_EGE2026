from math import *

def center(cluster):
    res = []
    for d1 in cluster:
        sum_dist = sum(dist(d1, d2) for d2 in cluster)
        res.append([sum_dist, d1])
    return min(res)[1]

with open(r'.\files\27_B_29074.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[2:] == 'V':
            target.append(dots[-1])

cluster_1 = [d for d in dots if d[1] > 22]
cluster_2 = [d for d in dots if 16 < d[1] < 22]
cluster_3 = [d for d in dots if d[0] > 22]

target_1 = [d for d in target if d[1] > 22]
target_2 = [d for d in target if 16 < d[1] < 22]
target_3 = [d for d in target if d[0] > 22]

B1 = min(
    [dist(center(cluster_1), d) for d in target_1] +
    [dist(center(cluster_2), d) for d in target_2] +
    [dist(center(cluster_3), d) for d in target_3]
)

B2 = max(
    [dist(center(cluster_1), d) for d in target_1] +
    [dist(center(cluster_2), d) for d in target_2] +
    [dist(center(cluster_3), d) for d in target_3]
)
print(B1 * 10_000, B2 * 10_000)

# 1738 20765