with open(r'.\files\17_25356.txt') as file:
    data = [int(i) for i in file]

max_30 = max(i for i in data if i % 100 == 30)

ans = []

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = not(1000 <= abs(num1) <= 9999)
    u2 = not(1000 <= abs(num2) <= 9999)
    u3 = not(1000 <= abs(num3) <= 9999)
    if u1 + u2 + u3 == 3:
        if num1 + num2 + num3 > max_30:
            ans += [num1 + num2 + num3]
print(len(ans), max(ans))

# 1032 285423