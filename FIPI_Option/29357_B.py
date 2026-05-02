from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_B_29357.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'K' and data[2:] == 'III':
            target.append(dots[-1])

cluster_1 = [d for d in dots if d[1] < 30]
cluster_2 = [d for d in dots if d[1] > 30 and d[0] < 16]
cluster_3 = [d for d in dots if d[0] > 16]

target_1 = [d for d in target if d[1] < 30]
target_2 = [d for d in target if d[1] > 30 and d[0] < 16]
target_3 = [d for d in target if d[0] > 16]

if max(target_1, target_2, target_3, key=len) == target_3:
    current_cluster_max = center(cluster_3)
elif max(target_1, target_2, target_3, key=len) == target_2:
    current_cluster_max = center(cluster_2)
else:
    current_cluster_max = center(cluster_1)

if min(target_1, target_2, target_3, key=len) == target_3:
    current_cluster_min = center(cluster_3)
elif min(target_1, target_2, target_3, key=len) == target_2:
    current_cluster_min = center(cluster_2)
else:
    current_cluster_min = center(cluster_1)

print(dist(current_cluster_max, current_cluster_min) * 10_000)

# 138716

with open(r'.\files\27_B_29357.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'G' and data[2:] == 'V':
            target.append(dots[-1])

cluster_1 = [d for d in dots if d[1] < 30]
cluster_2 = [d for d in dots if d[1] > 30 and d[0] < 16]
cluster_3 = [d for d in dots if d[0] > 16]

target_1 = [d for d in target if d[1] < 30]
target_2 = [d for d in target if d[1] > 30 and d[0] < 16]
target_3 = [d for d in target if d[0] > 16]
targets = [target_1, target_2, target_3]

B2 = max(dist(d1, d2) for line in targets for d1 in line for d2 in line)

print(B2 * 10_000)

# 34029