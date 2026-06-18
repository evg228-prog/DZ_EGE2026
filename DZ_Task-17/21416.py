with open(r'.\files\17_21416.txt') as file:
    data = [int(i) for i in file]

minn = [i for i in data if i < 0]

ans = []
for nums in zip(data, data[1:], data[2:]):
    if max(nums) * min(nums) > sum(minn):
        ans.append(sum(nums))
print(len(ans), abs(max(ans)))

# 10007 7953