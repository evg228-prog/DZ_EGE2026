from string import *

for x in printable[:15]:
    num1 = int(f'67845{x}65', 15)
    num2 = int(f'1{x}23456', 15)
    num3 = num1 + num2
    if num3 % 14 == 0:
        print(num3 // 14, x)

# 80788834