def f(start, end, cnt5, cnt3, cnt45):
    if cnt5 > 4: return 0
    if cnt45 > 5: return 0
    if start == end and cnt5 <= 4 and cnt3 >= 2 and cnt45 == 5: return 1
    if start > end: return 0
    return f(start * 5, end, cnt5 + 1, cnt3, cnt45) + \
            f(start * 3, end, cnt5, cnt3 + 1, cnt45) + \
            f(start + 45, end, cnt5, cnt3, cnt45 + 1)

print(f(1, 2970, 0, 0, 0))

# 74