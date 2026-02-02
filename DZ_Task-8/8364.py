from itertools import *

alph = sorted('крате')


for pos, val in set(enumerate(product(alph, repeat=6), start=1)):
    val = ''.join(val)
    if val == 'ракета':
        pos1 = pos
    if val == 'карета':
        pos2 = pos
print(abs(pos1 - pos2) - 1)

# 2999
