def f(start, end):
    if start == end: return 1
    if start > end: return 0
    return f(start + 1, end) + f(start * 2, end) + f(start * 3, end)

print(f(10, 30) * f(30, 70) + f(10, 60) * f(60, 70) -
      2 * f(10, 30) * f(30, 60) * f(60, 70))

# 95