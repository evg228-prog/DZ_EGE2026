from itertools import permutations

cnt = 0
for val in set(permutations('кидала', r=5)):
    val = ''.join(val)
    if 'аа' not in val:
        cnt += 1
print(cnt)

# 264