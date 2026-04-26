from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_B_29076.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
        if data[0] == 'Y':
            target.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 22]
cluster_2 = [d for d in dots if 16 < d[1] < 22]
cluster_3 = [d for d in dots if d[0] > 22]

target_1 = [d for d in target if d[1] > 22]
target_2 = [d for d in target if 16 < d[1] < 22]
target_3 = [d for d in target if d[0] > 22]

if len(target_1) < len(target_2) < len(target_3):
    minn = center(cluster_1)
elif len(target_2) < len(target_3) < len(target_1):
    minn = center(cluster_2)
else:
    minn = center(cluster_3)

if len(target_1) < len(target_2) < len(target_3):
    maxx = center(cluster_3)
elif len(target_2) < len(target_3) < len(target_1):
    maxx = center(cluster_1)
else:
    maxx = center(cluster_2)

maxx_2 = max(
    [dist(center(cluster_1), star) for star in target_1] +
    [dist(center(cluster_2), star) for star in target_2] +
    [dist(center(cluster_3), star) for star in target_3]
)

print(dist(minn, maxx) * 10_000, maxx_2 * 10_000)

# 125591 20077