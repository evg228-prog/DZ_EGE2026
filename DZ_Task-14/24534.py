from string import *

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

cnt_0 = []
for x in range(1, 11_500):
    num1 = convert(7**270 + 7**170 + 7**70 - x, 7)
    if str(num1).count('0') > 0:
        cnt_0.append([str(num1).count('0'), x])
print(max(cnt_0)[1])

# 9604