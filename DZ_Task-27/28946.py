from math import *

def center(cluster):
    res = []
    for d1 in cluster:
        sum_dist = sum(dist(d1, d2) for d2 in cluster)
        res.append([sum_dist, d1])
    return min(res)[1]

with open(r'.\files\27_A_28946.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
clusters_A = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 20:
        clusters_A.append(cluster)
maxx = max(clusters_A, key=len)
A1 = sum(1 for i in maxx if i[1] < center(maxx)[1])

minn = min(clusters_A, key=len)
A2 = abs(center(minn)[0] - center(maxx)[0])

print(A1, A2 * 10_000)

# 173 27601

with open(r'.\files\27_B_28946.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
clusters_B = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 20:
        clusters_B.append(cluster)

minn_2 = min(clusters_B, key=len)
x_c, y_c = center(minn_2)
B1 = sum(abs(x - x_c) <= 0.9 and abs(y - y_c) <= 0.9 for x, y in minn_2)

middle = sorted(clusters_B)[1]
maxx_2 = max(clusters_B, key=len)
B2 = abs(center(maxx_2)[1] - center(middle)[1])
print(B1, B2 * 10_000)

# 89 107171