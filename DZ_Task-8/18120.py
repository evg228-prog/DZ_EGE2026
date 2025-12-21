from itertools import product
from string import *

alph = sorted('престол')

cnt = 0
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0:
        if val[-1] in'ео' and (val.count('п') +  val.count('р') +  val.count('с') +  val.count('т') +  val.count('л') <= 3):
            cnt += 1
print(cnt)

# 1776