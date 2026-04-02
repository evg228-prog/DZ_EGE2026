from itertools import *



for x in range(1, 11):
    for pos, val in enumerate(product(sorted('сулак'), repeat=x), start=1):
        val = ''.join(val)
        if pos == 12368:
            if val[0] in 'лс':
                for i in 'ау': val = val.replace(i, '*')
                if val.count('*') <= 2 and '**' not in val:
                    print(x)

# 6