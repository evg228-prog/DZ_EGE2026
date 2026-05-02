from string import printable


def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num1 = convert(5 * 1296**2021 - 4 * 216**2022 + 3 * 36**2023 - 2 * 6**2024 - 2025, 36)

ans = 0
for i in num1:
    if int(i, 36) % 2 == 0:
        ans += 1
print(ans)

# 1013