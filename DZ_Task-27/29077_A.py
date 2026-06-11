from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_A_29077.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data == 'N9I':
            target.append(dots[-1])

cluster_1 = [d for d in dots if d[1] > 8]
cluster_2 = [d for d in dots if d[1] < 8]

target_1 = [d for d in target if d[1] > 8]
target_2 = [d for d in target if d[1] < 8]

c1 = center(cluster_1)
c2 = center(cluster_2)

if target_1:
    A1 = dist(c1, target_1[0])
    A2 = dist(c2, target_1[0])
else:
    A1 = dist(c1, target_2[0])
    A2 = dist(c2, target_2[0])
print(A1 * 10_000, A2 * 10_000)

# 1600 68648