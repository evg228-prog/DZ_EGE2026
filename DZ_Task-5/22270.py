ans = []
from string import printable
def convert(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
for N in range(1, 10000):
    R = convert(N, 4)
    if R[:1] == 3:
        R.count('1') * 3 and R.count('3') % 3
        R = '21' + R
    else:
        R = '1' + R[1:] + '12'
    R = int(R, 4)
    if R < 598:
        ans.append(N)
print(max(ans))

# 63