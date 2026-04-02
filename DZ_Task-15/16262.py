diap = 300

def f(A):
    for x in range(-diap, diap):
        for y in range(-diap, diap):
            F = ((A < x) or (x ** 2 - 7 * x + 10 > 0)) and ((A >= y) or (y ** 2 + 7 * y + 12 > 0))
            if not F:
                return False
    return True

cnt = 0

for A in range(-diap, diap):
    if f(A):
        cnt += 1
print(cnt)

##########################################################

def f(x, y):
    return ((A < x) or (x ** 2 - 7 * x + 10 > 0)) and ((A >= y) or (y ** 2 + 7 * y + 12 > 0))

cnt = 0
for A in range(-diap, diap):
    if all(f(x, y) for x in range(-diap, diap) for y in range(-diap, diap)):
        cnt += 1
print(cnt)