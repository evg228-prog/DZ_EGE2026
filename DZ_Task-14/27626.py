from string import *

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

cnt = 10 ** 10
for x in range(1, 2031):
    num1 = convert(6**2030 + 6**100 - x, 6)
    cnt = min(cnt, num1.count('0'))
print(cnt)

# 1930