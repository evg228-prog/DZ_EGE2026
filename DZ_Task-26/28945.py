with open(r'.\files\26_28945.txt') as file:
    N = int(file.readline())
    req = []
    for i in file:
        start, length = map(int, i.split())
        end = start + length
        req.append((start, end))
req = sorted(req, key=lambda x: x[1])
cnt = 0
cur_end = 0

for start, end in req:
    if start >= cur_end:
        cnt += 1
        cur_end = end

best_end = 0

for last_start, last_end in req:
    cnt_before = 0
    cur_end = 0
    for start, end in req:
        if end <= last_start and start >= cur_end:
            cnt_before += 1
            cur_end = end
    if cnt_before == cnt - 1:
        best_end = max(best_end, last_end)
print(cnt, 10_000 - best_end)

# 77 184


