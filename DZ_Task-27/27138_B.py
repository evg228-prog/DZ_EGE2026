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

res = []
for i in range(len(clusters)):
    current_cluster = clusters[i]
    other_clusters = clusters[:i] + clusters[i + 1:]
    other_clusters = [d for i in range(len(other_clusters)) for d in other_clusters[i]]
    for dot in current_cluster:
        sum_dist = sum(dist(dot, d) for d in other_clusters)
        res.append([sum_dist, dot])
B2 = sum(max(res)[1])

print(abs(int(cluster_med_X * 10000)), abs(int(B2 * 10000)))

# 434245 275003