from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]

with open(r'.\files\27_A_29357.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'M' and data[2:] == 'III':
            target.append(dots[-1])

cluster_1 = [d for d in dots if d[1] > 10]
cluster_2 = [d for d in dots if d[1] < 10]

target_1 = [d for d in target if d[1] > 10]
target_2 = [d for d in target if d[1] < 10]

if len(cluster_1) < len(cluster_2):
    minn = center(cluster_1)
    current_target = target_1
else:
    minn = center(cluster_2)
    current_target = target_2
# [dist(minn, x) for x in minn]
rasst = min(current_target, [dist(minn, x) for x in minn])
print(rasst[0] * 10_000, rasst[1] * 10_000)

# 44694 69754