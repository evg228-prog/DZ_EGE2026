def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if i != num:
                d |= {i}
            if num // i != num:
                d |= {num // i}
    return sum(d) // len(d)

cnt = 0
for N in range(1, 770000)[::-1]:
    A = f(N)
    if A % 100 == 12:
        print(N, A)
        cnt += 1
        if cnt == 5:
            break

# 769995 25612
# 769923 18312
# 769916 35712
# 769700 27112
# 769583 2912