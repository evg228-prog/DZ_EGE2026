from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_A_28766.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Y' and data[2:].strip() == 'III':
            target.append(list(map(float, [x, y])))

cluster_1 = [dot for dot in dots if dot[1] < 8]
cluster_2 = [dot for dot in dots if dot[1] > 8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

minn = center(min(cluster_1, cluster_2, key=len))
ans = [dist(minn, d) for d in target]
print(min(ans) * 10_000, max(ans) * 10_000)

# 4940 74302