from itertools import *

alph = sorted('аргумент')
print(alph)
for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if val == ''.join(sorted(val)) and len(val) == len(set(val)):
        print(pos, val)

# 2424