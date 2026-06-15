from itertools import *

alph = sorted('фокус')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if 'ф' not in val and val.count('у') == 2:
        print(pos, val)

# 2313