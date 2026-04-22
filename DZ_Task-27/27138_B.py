from math import *

def center(cluster, other_1, other_2):
    res = []
    for dot1 in cluster:
        sum_dist = 0
        for dot2 in other_1 + other_2:
            sum_dist += dist(dot1, dot2)
        res.append([sum_dist, dot1])
    return max(res)

with open(r'.\files\27B_27138.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 2
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

clusters = sorted(clusters, key=len)

cluster_med = clusters[1]
cluster_med_X = max(cluster[0] for cluster in cluster_med)

cluster_anti_1 = center(clusters[0], clusters[1], clusters[2])
cluster_anti_2 = center(clusters[1], clusters[0], clusters[2])
cluster_anti_3 = center(clusters[2], clusters[0], clusters[1])

cluster_anti = max(cluster_anti_1, cluster_anti_2, cluster_anti_3)[1]

print(abs(int(cluster_med_X * 10000)), abs(int(sum(cluster_anti) * 10000)))