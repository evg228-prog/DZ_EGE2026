from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
R = str(convert(51 * 7**12 - 7**3 - 22, 7))
print(sum(map(int, R)))

# 70