from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 17: return 6
    return (n + 5) * F(n - 9)

for i in range(234570):
    F(i)

print((F(234561) // 436 + F(234552) // 218) // F(234534))