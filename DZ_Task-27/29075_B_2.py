from math import *

def center(cluster):
    res = []
    for d1 in cluster:
        sum_dist = sum(dist(d1, d2) for d2 in cluster)
        res.append([sum_dist, d1])
    return min(res)[1]

with open(r'.\files\27_B_29075.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'J':
            target.append(dots[-1])

cluster_1 = [d for d in dots if d[1] > 22]
cluster_2 = [d for d in dots if 16 < d[1] < 22]
cluster_3 = [d for d in dots if d[0] > 22]

target_1 = [d for d in target if d[1] > 22]
target_2 = [d for d in target if 16 < d[1] < 22]
target_3 = [d for d in target if d[0] > 22]

B1 = min(
    min(dist(d1, d2) for d1 in target_1 for d2 in target_2),
    min(dist(d1, d2) for d1 in target_2 for d2 in target_3),
    min(dist(d1, d2) for d1 in target_3 for d2 in target_1)
)

B2 = max(
    max(dist(d1, d2) for d1 in target_1 for d2 in target_2),
    max(dist(d1, d2) for d1 in target_2 for d2 in target_3),
    max(dist(d1, d2) for d1 in target_3 for d2 in target_1)
)

print(B1 * 10_000, B2 * 10_000)

# 54383 217885