from string import *

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for x in range(1, 27001):
    num1 = convert(3 * 27**9 + 2 * 27**6 + 27**3 - x, 27)
    if num1.count('0') == 6:
        print(x)
        break