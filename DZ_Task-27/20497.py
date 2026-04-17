from math import *

def anticenter(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return max(res)[1]

with open(r'.\files\27.19.A_20497.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 0.5
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters += [cluster]

print([len(cluster) for cluster in clusters])
anticenters = [anticenter(cluster) for cluster in clusters]
anticenters_A_X = [anticenter(cluster)[0] for cluster in clusters]
anticenters_A_Y= [anticenter(cluster)[1] for cluster in clusters]
print(sum(anticenters_A_X) / len(anticenters_A_X) * 10_000, sum(anticenters_A_Y) / len(anticenters_A_X) * 10_000)

# 13258 2656

with open(r'.\files\27.19.B_20497.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 4
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters += [cluster]

print([len(cluster) for cluster in clusters])
anticenters = [anticenter(cluster) for cluster in clusters]
anticenters_A_X = [anticenter(cluster)[0] for cluster in clusters]
anticenters_A_Y= [anticenter(cluster)[1] for cluster in clusters]
print(sum(anticenters_A_X) / len(anticenters_A_X) * 10_000, sum(anticenters_A_Y) / len(anticenters_A_X) * 10_000)

# 209434 474989