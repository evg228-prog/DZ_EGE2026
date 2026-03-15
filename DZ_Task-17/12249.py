with open(r'.\files\17_12249.txt') as file:
    data = [int(i) for i in file]

max_3 = max(i for i in data if abs(i) % 10 == 3 and 10000 <= i <= 99999)

ans = []

for num1, num2, num3 in zip(data, data[1:], data[2:]):
    if ((abs(num1) % 10 == 3) + (abs(num2) % 10 == 3) + (abs(num3) % 10 == 3)) >= 1 and (num1 + num2 + num3) <= max_3:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))


