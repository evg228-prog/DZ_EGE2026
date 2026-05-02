with open(r'.\files\17_29349.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if i > 0 and i % 123 == 0)

ans = []
for nums in zip(data, data[1:]):
    if sum(nums) < minn:
        ans.append(sum(nums))
print(len(ans), abs(max(ans)))

# 5001 962