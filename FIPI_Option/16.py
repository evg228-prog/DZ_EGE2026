from functools import *

@lru_cache(None)
def F(n):
    if n < 10: return 1
    return (n + 3) * F(n - 3)

for i in range(1, 247564):
    F(i)

print((F(247563) // 519 - 477 * F(247560)) // F(247557))

# 1431