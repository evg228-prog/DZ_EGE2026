from string import printable as olo
def convert(num, sys):
    res = ''
    while num:
        res += olo[num % sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N, 7)
    if R[-1] == '2':
        R = R.replace('3', '*')
        R = R.replace('1', '3')
        R = R.replace('*', '1')
        R = '21' + R
    else:
        R = '1' + R[1:] + '36'
    R = int(R, 7)
    if R < 744:
        ans.append([R, N])
max_R = max(ans)[0]
all_N = []
for i in ans:
    if max_R == i[0]:
        all_N.append(i[1])
print(min(all_N))

# 13