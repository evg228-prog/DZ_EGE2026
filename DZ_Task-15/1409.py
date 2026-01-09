from itertools import *

def f(x):
    P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    R = {12, 24, 36, 48, 60}
    A = A1 <= x <= A2
    return (not A) <= ((P and Q) <= R)

line = range(1, 61)

ans = []
for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(ans)

