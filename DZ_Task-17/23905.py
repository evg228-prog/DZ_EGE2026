with open(r'.\files\17_23905.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if abs(i) % 100 == 37)

ans = []
num_equals = []
for nums in zip(data, data[1:], data[2:], data[3:]):
    u1 = sum(1 for num in nums if num > maxx) == 2
    u2 = [num for num in nums if abs(num) >= 10 and str(abs(num))[-1] == str(abs(num))[-2]]
    if u1 and len(u2) == 1:
        ans.append(nums)
        num_equals.append(u2[0])
print(len(ans), sum(num_equals))

# 13 110680