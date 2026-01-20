from itertools import *

def f(x):
    M = 32 <= x <= 68
    N = 54 <= x <= 76
    A = A1 <= x <= A2
    return (not (M or N)) == (not A)

line = [x + eps for x in range(32, 77) for eps in (0, 0.1, 0.9)]

ans = []
for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))

# 44