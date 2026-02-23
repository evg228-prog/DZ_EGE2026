def f(pos, steps):
     if steps == 15: return {pos}
     return f(pos + 10, steps + 1) | f(pos - 5, steps + 1)

print(len(f(1, 0)))

# 16