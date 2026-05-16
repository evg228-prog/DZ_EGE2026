with open(r'.\files\24_7438.txt') as file:
     data = file.readline()

ans = 0
l = 0

while l < len(data):
    r = l
    cnt_D = 0
    while r < len(data):
        if data[r].isdigit():
            break
        if r > l and data[r - 1: l + 1] in ('DC', 'SD'):
            break
        if data[r] == 'D':
            cnt_D += 1
        if cnt_D > 100:
            break
        if cnt_D == 100:
            ans = max(ans, r - l + 1)
        r += 1
    l += 1
print(ans)

# 644