def DEL(n, m):
    return n % m == 0

def f(x):
    return (DEL(x, 3) <= (not DEL(x, 5))) or (x + A >= 70)

for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break

# 55