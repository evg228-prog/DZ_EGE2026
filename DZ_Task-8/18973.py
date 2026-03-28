from itertools import product
from string import *

digits = digits + ascii_uppercase[:15]

cnt = 0

for val in product(digits, repeat=4):
    if val[0] != '0':
        u1 = any(i in digits[::2] for i in val)
        u2 = sum(i in digits[16:] for i in val) >= 3
        if u1 and u2:
            cnt += 1
print(cnt)

# 50184