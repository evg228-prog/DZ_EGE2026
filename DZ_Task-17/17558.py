with open(r'.\files\17_17558.txt') as file:
    data = [int(i) for i in file]

cnt_32 = sum(1 for i in data if abs(i) % 32 == 0)

ans = []
for nums in zip(data, data[1:]):
    u1 = sum(1 for num in nums if str(num)[0] == '-') >= 1
    u2 = sum(nums) < cnt_32
    if u1 and u2:
        ans.append(sum(nums))
print(len(ans), max(ans))

# 4969 299