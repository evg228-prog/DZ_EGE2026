with open(r'.\files\17_23276.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if abs(i) % 100 == 25)

ans = []
for nums in zip(data, data[1:], data[2:]):
    u1 = sum(1 for num in nums if 1000 <= abs(num) <= 9999) <= 2
    u2 = sum(nums) <= maxx
    if u1 and u2:
        ans += [sum(nums)]
print(len(ans), max(ans))

# 6315 84523
