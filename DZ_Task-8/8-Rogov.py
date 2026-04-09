from itertools import *

alph = sorted('кофе')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('о') == 1:
        for i in 'кф': val = val.replace(i, '*')
        if 'о*' not in val and '*о' not in val and '*о*' not in val:
            print(pos)

# 1014