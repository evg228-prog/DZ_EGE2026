from string import printable as olo
def convert(num, sys):
    res = ''
    while num:
        res += olo[num % sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N, 5)
    if R.endswith('0'):
        R = R.replace('1', '*')
        R = R.replace('4', '1')
        R = R.replace('*', '4')
        R = '33' + R
    else:
        R = '3' + R[1:] + '42'
    R = int(R, 5)
    if R < 1922:
        ans.append(R)

max_R = max(ans)
all_N = []
for i in ans:
    if max_R == i:
        all_N.append(i[1])
print(min(all_N))


# 9