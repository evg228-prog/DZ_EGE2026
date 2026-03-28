from string import *
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res [::-1]

for y in range(1, 100):
    for x in range(1, 100):
        num1 = 5**50 + 5**30 - 5**x - y - 5**y - x
        if num1 > 0 and convert(num1, 5).count('0') == 10:
            print(x * y)

# 1960