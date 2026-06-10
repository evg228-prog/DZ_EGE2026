from string import *

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for x in range(1, 2400):
    num_cur = convert(7 * 9**210 + 6 * 9**110 - x, 9)
    if str(num_cur).count('0') == 100:
        print(x)

# 2394