def DIG(x, y):
    return str(x)[0] == str(y)[0]

def f(A):
    for x in range(1, 1000):
        F = ((not DIG(x, 28)) and DIG(x, 47)) <= (x > A - 20)
        if not F:
            return False
    return True

for A in range(1, 1000)[::-1]:
    if f(A):
        print(A)
        break

# 23