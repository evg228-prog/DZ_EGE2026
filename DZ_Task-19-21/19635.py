def f(x, y, s):
    if x + y <= 100: return s % 2 == 0
    if s == 0: return 0
    h = [f(x - 3, y - 3, s - 1),
         f(x // 2, y, s - 1),
         f(x, y // 2, s - 1)]
    if x % 2 != 0:
        f(x // 2 - 1, y, s - 1)
    if y % 2 != 0:
        f(x, y // 2 - 1, s - 1)
    return any(h) if (s - 1) % 2 == 0 else any(h)

print('19)', [x for x in range(53, 300) if f(48, x, 2)])
print('20)', [x for x in range(52, 300) if f(48, x, 3) and not f(48, x, 1)])
print('21)', [x for x in range(52, 300) if f(48, x, 4) and not f(48, x, 2)])

# 19) 59
# 20) 115 229
# 21) 124