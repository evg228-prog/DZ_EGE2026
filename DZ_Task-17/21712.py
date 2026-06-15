with open(r'.\files\17_21712.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if i > 0 and abs(i) % 10 == 6 and 1000 <= abs(i) <= 9999)

ans = []
for nums in zip(data, data[1:], data[2:]):
    u1 = sum(1 for num in nums if 1000 <= abs(num) <= 9999 and abs(num) % 10 == 6) == 1
    u2 = sum(nums) <= minn
    if u1 and u2:
        ans.append(sum(nums))
print(len(ans), max(ans))

# 507 1042