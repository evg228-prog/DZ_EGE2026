with open(r'.\files\26_29234.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = (sorted(enumerate(times), key=lambda x: (x[1][0], x[1])))

end_time = [0] * (K + 1)
profit = [0] * (K + 1)
cnt = 0

for index, (start, end) in times:
    comp = 0
    for i in range(1, K + 1):
        if end_time[i] < start:
            comp = i
            break
    if comp != 0:
        end_time[comp] = end
        t = end - start
        profit[comp] += t * (t + 1) // 2
        cnt += 1
print(cnt, max(profit))

# 3775 54798