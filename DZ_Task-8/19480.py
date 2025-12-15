from itertools import permutations

cnt = 0
for val in set(permutations('парижанка')):
    val = ''.join(val)
    if sum(val[i] in 'аи' and val[i + 1] in 'аи' for i in range(len(val)-1)) == 1:
        cnt += 1
print(cnt)

# 28800