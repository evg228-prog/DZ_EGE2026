from itertools import *

alph = sorted('бмюрн')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] != 'м' and val.count('р') >= 2 and 'ю' not in val:
        if pos % 2 != 0:
            print(pos)

# 11719