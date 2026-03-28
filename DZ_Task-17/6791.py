with open(r'.\files\17_6791.txt') as file:
    data = [int(i) for i in file]

min_68 = min(i for i in data if abs(i) % 100 == 68)

ans = []

for nums in zip(data, data[1:]):
    u1 = sum(abs(num) % 100 == 68 for num in nums) == 1
    u2 = sum(num ** 2 for num in nums) >= min_68 ** 2
    if u1 and u2:
        ans.append(sum(num ** 2 for num in nums))
print(len(ans), max(ans))

# 26 188357305