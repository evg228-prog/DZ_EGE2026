from itertools import *
alph = sorted('парус')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] == 'у' and 'аа' not in val:
        print(pos)
        break

# 2527