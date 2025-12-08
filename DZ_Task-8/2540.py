from itertools import *
alph = sorted('автор')

for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if val[0] == 'в' and val[1] == 'а' and val[2] == 'т' and val[3] == 'а':
        print(pos)

# 146