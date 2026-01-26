from string import *
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for x in range(1, 2005):
    num1 = convert(4**163 * 5 + 12**62 - x, 5)
    if num1.count('1') < num1.count('4'):
        print(x)

# 2000