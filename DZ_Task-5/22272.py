from string import *

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N, 9)
    if R[0] == '7':
        R = R.replace('6', '*')
        R = R.replace('3', '6')
        R = R.replace('*', '3')
        R = '34' + R[2:]
    else:
        R = '3' + R[1:] + '45'
    R = int(R, 9)
    if R < 2876:
        ans.append([R, N])
print(max(ans))