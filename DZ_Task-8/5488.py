from itertools import *
alph = sorted('полина')

cnt = 0
for pos, val in enumerate(product(alph, repeat=8), start=1):
    val = ''.join(val)
    if (val.count('п') + val.count('л') + val.count('н')) > (val.count('о') + val.count('и') + val.count('а')):
        cnt += 1
print(cnt)

# 610173