ans = set()

for A in range(625, 3125):
    for B in range(625, A):
        ans.add(A - B)
print(len(ans))

# 2499