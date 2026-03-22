def f(pos, steps):
    if steps == 13: return {pos} if pos < 0 else set()
    return f(pos - 3, steps + 1) | f(pos * (-3), steps + 1)

print(len(f(333, 0)))

# 2224