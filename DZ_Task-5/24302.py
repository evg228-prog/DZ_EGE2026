from string import *

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N, 3)
    if sum(map(int, R)) % 9 == 0:
        R += '2'
    else:
        R += convert(sum(map(int, R)) % 9, 3)
    R = int(R, 3)
    if N > 166:
        ans.append(R)
print(min(ans))

# 647