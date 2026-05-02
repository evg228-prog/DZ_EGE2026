from itertools import *

alph = sorted('апрель')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 != 0:
        if val[0] not in 'ал' and val.count('п') >= 2:
            print(pos)
            break

# 7903