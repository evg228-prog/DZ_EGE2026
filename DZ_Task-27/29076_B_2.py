from math import *

def center(cluster):
    res = []
    for d1 in cluster:
        sum_dist = sum(dist(d1, d2) for d2 in cluster)
        res.append([sum_dist, d1])
    return min(res)[1]

with open(r'.\files\27_B_29076.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Y':
            target.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 22]
cluster_2 = [d for d in dots if 16 < d[1] < 22]
cluster_3 = [d for d in dots if d[0] > 22]

target_1 = [d for d in target if d[1] > 22]
target_2 = [d for d in target if 16 < d[1] < 22]
target_3 = [d for d in target if d[0] > 22]

if min(target_1, target_2, target_3, key=len) == target_1:
    minn = center(cluster_1)
elif min(target_1, target_2, target_3, key=len) == target_2:
    minn = center(cluster_2)
else:
    minn = center(cluster_3)

if max(target_1, target_2, target_3, key=len) == target_1:
    maxx = center(cluster_1)
elif max(target_1, target_2, target_3, key=len) == target_2:
    maxx = center(cluster_2)
else:
    maxx = center(cluster_3)

B1 = dist(minn, maxx)

B2 = max(
    max(dist(center(cluster_1), d) for d in target_1),
    max(dist(center(cluster_2), d) for d in target_2),
    max(dist(center(cluster_3), d) for d in target_3)
)

print(B1 * 10_000, B2 * 10_000)

# 125591 20077