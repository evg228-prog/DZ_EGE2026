from itertools import permutations

cnt = 0
for val in set(permutations('амфибрахий')):
    val = ''.join(val)
    if 'иифаа' in val or 'аафии' in val:
        cnt += 1
print(cnt)

# 1440