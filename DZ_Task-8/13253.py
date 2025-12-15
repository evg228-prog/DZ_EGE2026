from itertools import *

const1 = {''.join(val) for val in product('конец', repeat=5)}
const2 = {''.join(val) for val in product('дракон', repeat=5)}

count = len(const1 - const2) + len(const2 - const1)

print(count)

# 10415