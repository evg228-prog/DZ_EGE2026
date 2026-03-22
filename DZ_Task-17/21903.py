with open(r'.\files\17_21903.txt') as file:
    data = [int(i) for i in file]

min_15 = min(i for i in data if abs(i) % 100 == 15 and 100 <= abs(i) <= 999)

ans = []

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = (num1 < 0 and num2 < 0 and num3 < 0) or (num1 > 0 and num2 > 0 and num3 > 0)
    u2 = min(num1, num2, num3) * max(num1, num2, num3) > min_15 ** 2
    if u1 and u2:
        ans.append(min(num1, num2, num3) * max(num1, num2, num3))
print(len(ans), min(ans))
