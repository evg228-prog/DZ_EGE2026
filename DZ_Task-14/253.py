from string import printable as klk
def convert(num, sys):
    res = ''
    while num:
        res += klk[num % sys]
        num //= sys
    return res[::-1]
print(convert(41, 13))
print(convert(131, 13))

# 13