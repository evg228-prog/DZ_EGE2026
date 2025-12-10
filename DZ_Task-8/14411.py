from itertools import *
alph = sorted('сублимаця')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[-1] != 'я' and ((val.count('у') + val.count('и') + val.count('а') + val.count('я')) == 2):
        if pos % 2 != 0:
            print(pos)

# 58955