from itertools import *
alph = sorted('дионсй')

cnt = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if ((val.count('д') >= 1 and val.count('н') == 0) or (val.count('н') >= 1 and val.count('д') == 0)) and ('дд' not in val and 'ии' not in val and
        'оо' not in val and 'нн' not in val and 'сс' not in val and 'йй' not in val):
        cnt += 1
print(cnt)

# 8296
