from string import *
def convert(num, sys):
    res = ''
    while num:
        res += sys[num % sys]
        num //= sys
    return res[::-1]

for x in printable[:25]:
    num1 = int(f'11353{x}12', 25)
    num2 = int(f'135{x}21', 25)
    num3 = num1 + num2
    if num3 % 24 == 0:
        print(x, num3 // 24)

# 266249847