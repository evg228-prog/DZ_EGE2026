with open(r'.\files\17_16383.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if 10_000 <= abs(i) <= 99_999 and abs(i) % 100 == 21)

ans = []
for nums in zip(data, data[1:]):
    u1 = sum(1 for num in nums if abs(num) % 100 == 21 and 10_000 <= abs(num) <= 99_999) == 1
    u2 = sum(num ** 2 for num in nums) >= maxx ** 2
    if u1 and u2:
        ans.append(sum(nums))
print(len(ans), max(ans))

# 74 103365