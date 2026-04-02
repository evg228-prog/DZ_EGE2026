with open(r'.\files\17_21595.txt') as file:
    data = [int(i) for i in file]

cnt_max = [i for i in data if 1000 <= abs(i) <= 9999 and abs(i) % 10 == 3]

ans = []

for nums in zip(data, data[1:], data[2:]):
    nums = sorted(nums)
    if nums[1] + nums[2] > len(cnt_max) ** 2:
        ans.append(abs(sum(nums)))
print(len(ans), max(ans))

# 7236 286698

