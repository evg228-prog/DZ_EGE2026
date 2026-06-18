from string import *

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for x in range(1, 5555)[::-1]:
    num1 = convert(5**150 + 5**135 - x, 5)
    if num1.count('4') == 134:
        print(x)
        break

# 3126