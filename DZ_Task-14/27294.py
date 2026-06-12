from string import *

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

cnt = 0
for x in range(1, 9431):
    num1 = convert(39**483 + 39**235 - x, 39)
    cnt = max(cnt, num1.count('0'))
print(cnt)

# 250