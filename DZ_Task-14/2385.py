from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
R = convert(16**820 - 2**761 + 14, 4)
new_R = R[1:].count('0')
print(new_R)

# 378