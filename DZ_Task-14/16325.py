from string import *
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num1 = convert(2 * 729**2014 + 2 * 243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2 * 9**2022 - 2024, 27)
cnt = 0
for i in num1:
    if i.isalpha():
        cnt += 1
print(cnt)

# 2687