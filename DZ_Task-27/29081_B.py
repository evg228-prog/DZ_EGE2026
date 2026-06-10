from itertools import combinations
from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_B_29081.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] in '89':
            target.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 24]
cluster_2 = [d for d in dots if 16 < d[1] < 22]
cluster_3 = [d for d in dots if d[0] > 22]

target_1 = [d for d in target if d[1] > 24]
target_2 = [d for d in target if 16 < d[1] < 22]
target_3 = [d for d in target if d[0] > 22]


B1 = min(
    min(dist(d1, d2) for d1 in target_1 for d2 in target_2),
    min(dist(d1, d2) for d1 in target_1 for d2 in target_3),
    min(dist(d1, d2) for d1 in target_3 for d2 in target_2)
)

targets = [target_1, target_2, target_3]
rasst = []
for target in targets:
    for d1, d2 in combinations(target, 2):
        rasst.append(dist(d1, d2))
B2 = sum(rasst) / len(rasst)

print(B1 * 10_000, B2 * 10_000)

# 54154 11641