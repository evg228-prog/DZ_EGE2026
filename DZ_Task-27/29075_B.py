from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_B_29075.txt') as file:
    dots = []
    target =[]
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'J':
            target.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 22]
cluster_2 = [d for d in dots if 16 < d[1] < 22]
cluster_3 = [d for d in dots if d[0] > 22]

target_1 = [d for d in target if d[1] > 22]
target_2 = [d for d in target if 16 < d[1] < 22]
target_3 = [d for d in target if d[0] > 22]

minn = min(
    [dist(dot1, dot2) for dot1 in target_1 for dot2 in target_2] +
    [dist(dot1, dot2) for dot1 in target_1 for dot2 in target_3] +
    [dist(dot1, dot2) for dot1 in target_3 for dot2 in target_2]
)

maxx = max(
    [dist(dot1, dot2) for dot1 in target_1 for dot2 in target_2] +
    [dist(dot1, dot2) for dot1 in target_1 for dot2 in target_3] +
    [dist(dot1, dot2) for dot1 in target_3 for dot2 in target_2]
)

print(minn * 10_000, maxx * 10_000)

# 54383 217885