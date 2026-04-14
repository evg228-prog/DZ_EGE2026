from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_B_17915.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [dot for dot in dots if 6 < dot[0] < 12 and 16 < dot[1] < 21]
cluster_2 = [dot for dot in dots if 10 < dot[0] < 15 and 4 < dot[1] < 9]
cluster_3 = [dot for dot in dots if 15 < dot[0] < 21 and 5 < dot[1] < 11]
cluster_4 = [dot for dot in dots if 23 < dot[0] < 28 and 15 < dot[1] < 20]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)
center_4 = center(cluster_4)

print((center_1[0] + center_2[0] + center_3[0]  + center_4[0]) / 4 * 10_000)
print((center_1[1] + center_2[1] + center_3[1]  + center_4[1]) / 4 * 10_000)

# 163215 128141
