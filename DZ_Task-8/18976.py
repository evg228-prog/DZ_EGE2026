from itertools import product
from string import printable

cnt = 0
for val in product(printable[:20], repeat=5):
    if val[0] != '0' and sum(map(int, val[-2:])) == 26:
        val = ''.join(['*' if i in '02468ACEGI' else '+' for i in val])
        if val == '+*+*+' or val == '*+*+*':
            cnt += 1
print(cnt)