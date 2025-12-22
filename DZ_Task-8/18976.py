from itertools import product
from string import printable

cnt = 0
for val in product(printable[:20], repeat=5):
    if val[0] != '0':
        val_1 = int(val[0], 20)
        val_5 = int(val[-1], 20)
        if val_1 + val_5 == 26:
            val = ''.join(['*' if i in '02468acegi' else '+' for i in val])
            if val == '+*+*+' or val == '*+*+*':
                cnt += 1
print(cnt)

# 13000